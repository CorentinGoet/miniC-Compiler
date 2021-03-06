"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""
from lexer_pkg.lexem import LexemTag
from AST import *


class Parser:
    """
    The parser_pkg takes the lexems from the lexer and builds the AST.
    """

    def __init__(self):
        self.lexems = []

    def peek(self, n: int = 0):
        """
        Returns the nth next lexem without consuming it.
        """
        if len(self.lexems) > n:
            return self.lexems[n]
        else:
            raise ValueError("No more lexems to peek.")

    def expect(self, tag: LexemTag):
        """
        pops the next lexem and tests its type.
        """
        lexem = self.peek()
        if lexem.tag == tag:
            return self.accept()
        else:
            raise TypeError("Error: expected {} but got {}".format(tag, lexem.tag))

    def accept(self):
        """
        Accepts the next lexem and returns it.
        """
        return self.lexems.pop(0)

    def parse(self, lexems):
        """
        Parses the lexems and returns the AST.
        """
        self.lexems = lexems
        return self.parse_program()

    def parse_program(self):
        """
        Parses the program lexem.
        The program has the syntax "int main(){ Declarations Statements }"
        """
        self.expect(LexemTag.TYPE)
        self.expect(LexemTag.MAIN)
        self.expect(LexemTag.L_PARENTHESIS)
        self.expect(LexemTag.R_PARENTHESIS)
        self.expect(LexemTag.L_BRACE)

        declarations = self.parse_declarations()
        statements = self.parse_statements()

        program = Program(declarations, statements)

        self.expect(LexemTag.R_BRACE)

        self.ast = program
        return program

    def parse_declarations(self):
        """
        Parses the declarations lexem.

        The declarations have the syntax "{ Declaration }"
        """
        declarations = []
        while True:
            try:
                declarations.append(self.parse_declaration())
            except TypeError:
                # The parser_pkg found a non declaration lexem, so we stop parsing declarations
                break
            except ValueError:
                # No more lexems to peek
                break
        return Declarations(declarations)

    def parse_declaration(self):
        """
        Parses the declaration lexem.

        The declaration has the syntax "type id;"
        """
        type = self.parse_type()
        identifiers = [self.parse_identifier()]
        if self.peek().tag == LexemTag.COMMA:
            # We have multiple identifiers
            while True:
                self.expect(LexemTag.COMMA)
                id = self.parse_identifier()
                identifiers.append(id)
                if self.peek().tag != LexemTag.COMMA:
                    break
        self.expect(LexemTag.TERMINATOR)
        return Declaration(type, identifiers)

    def parse_type(self):
        """
        Parses the type lexem.

        The type has the syntax "int|float|bool|char"
        """
        t = self.expect(LexemTag.TYPE)
        return Type(t.value)

    def parse_identifier(self):
        """
        Parses the identifier lexem.

        The identifier has the syntax "Letter{Letter|Digit}"
        """
        identifier = self.expect(LexemTag.IDENTIFIER)
        return Identifier(identifier.value)

    def parse_statements(self):
        """
        Parses the statements lexem.

        The statements has the syntax "{Statement}"
        """
        statements = []
        while True:
            try:
                if self.peek().tag == LexemTag.R_BRACE:
                    break
                if self.peek().tag != LexemTag.TERMINATOR:
                    statements.append(self.parse_statement())
            except ValueError:
                # No more lexems to peek
                break
        return Statements(statements)

    def parse_statement(self):
        """
        Parses the statement lexem.

        The statement can be an if statement, a while statement, or an assignment.
        """
        next_lexem = self.peek()
        if next_lexem.tag == LexemTag.IF_kw:
            return Statement(self.parse_ifStatement())
        elif next_lexem.tag == LexemTag.WHILE_kw:
            return Statement(self.parse_whileStatement())
        else:
            try:
                return Statement(self.parse_assignment())
            except Exception:
                raise TypeError("{} is not a valid statement.".format(next_lexem))

    def parse_ifStatement(self):
        """
        Parses the ifStatement lexem.

        The if statement has the syntax "if(Expression){Statement}[else{Statement}]"
        """
        self.expect(LexemTag.IF_kw)
        self.expect(LexemTag.L_PARENTHESIS)
        expression = self.parse_expression()
        self.expect(LexemTag.R_PARENTHESIS)
        self.expect(LexemTag.L_BRACE)
        statement = self.parse_statement()
        self.expect(LexemTag.R_BRACE)
        if self.peek().tag == LexemTag.ELSE_kw:
            self.expect(LexemTag.ELSE_kw)
            self.expect(LexemTag.L_BRACE)
            else_statement = self.parse_statement()
            self.expect(LexemTag.R_BRACE)
            return IfStatement(expression, statement, else_statement)
        else:
            return IfStatement(expression, statement)

    def parse_whileStatement(self):
        """
        Parses the whileStatement lexem.

        The while statement has the syntax: "while(Expression){Statement}"
        """
        self.expect(LexemTag.WHILE_kw)
        self.expect(LexemTag.L_PARENTHESIS)
        expression = self.parse_expression()
        self.expect(LexemTag.R_PARENTHESIS)
        self.expect(LexemTag.L_BRACE)
        statement = self.parse_statements()
        self.expect(LexemTag.R_BRACE)
        return WhileStatement(expression, statement)

    def parse_assignment(self):
        """
        Parses the assignment lexem.

        The assignment has the syntax: "id = Expression;"
        """
        identifier = self.parse_identifier()
        self.expect(LexemTag.ASSIGNMENT)
        expression = self.parse_expression()
        self.expect(LexemTag.TERMINATOR)
        return Assignment(identifier, expression)

    def parse_expression(self):
        """
        Parses the expression lexem.

        The expression has the syntax: "Conjunction{ || Conjunction}"
        """
        conjunctions = []
        conjunctions.append(self.parse_conjunction())
        while self.peek().tag == LexemTag.OR:
            self.expect(LexemTag.OR)
            conjunctions.append(self.parse_conjunction())
        return Expression(conjunctions)

    def parse_conjunction(self):
        """
        Parses the conjunction lexem.

        The conjunction has the syntax: "Equality{ && Equality}"
        """
        equalities = []
        equalities.append(self.parse_equality())
        while self.peek().tag == LexemTag.AND:
            self.expect(LexemTag.AND)
            equalities.append(self.parse_equality())
        return Conjunction(equalities)

    def parse_equality(self):
        """
        Parses the equality lexem.

        The equality has the syntax: "Relation [ EquOp Relation ]"
        """
        relation = self.parse_relation()
        if self.peek().tag == LexemTag.EQUAL or self.peek().tag == LexemTag.NOT_EQUAL:
            equ_op = self.parse_equop()
            relation2 = self.parse_relation()
            return Equality(relation, equ_op, relation2)
        return Equality(relation)
    
    def parse_equop(self):
        """
        Parses the equop lexem.
        """
        if self.peek().tag == LexemTag.EQUAL:
            self.expect(LexemTag.EQUAL)
            return EquOp(EquOp.equal)
        elif self.peek().tag == LexemTag.NOT_EQUAL:
            self.expect(LexemTag.NOT_EQUAL)
            return EquOp(EquOp.unequal)
        else:
            raise ValueError("{} is not a valid equality operator.".format(self.peek()))

    def parse_relation(self):
        """
        Parses the relation lexem.

        The relation has the syntax: "Addition [ RelOp Addition ]"
        """
        addition = self.parse_addition()
        if self.peek().tag in [LexemTag.LESS, LexemTag.LESS_EQUAL, LexemTag.GREATER, LexemTag.GREATER_EQUAL]:
            rel_op = self.parse_relop()
            addition2 = self.parse_addition()
            return Relation(addition, rel_op, addition2)
        return Relation(addition)

    def parse_relop(self):
        """
        Parses a relop lexem.
        """
        if self.peek().tag == LexemTag.LESS:
            self.expect(LexemTag.LESS)
            return RelOp(RelOp.INF)
        elif self.peek().tag == LexemTag.LESS_EQUAL:
            self.expect(LexemTag.LESS_EQUAL)
            return RelOp(RelOp.INFEQ)
        elif self.peek().tag == LexemTag.GREATER:
            self.expect(LexemTag.GREATER)
            return RelOp(RelOp.SUP)
        elif self.peek().tag == LexemTag.GREATER_EQUAL:
            self.expect(LexemTag.GREATER_EQUAL)
            return RelOp(RelOp.SUPEQ)
        else:
            raise ValueError("{} is not a valid relation operator.".format(self.peek()))

    def parse_addition(self):
        """
        Parses the addition lexem.

        The addition has the syntax: "Term { AddOp Term }"
        """
        terms = []
        operators = []
        terms.append(self.parse_term())
        while self.peek().tag == LexemTag.ADDITION or self.peek().tag == LexemTag.SUBTRACTION:
            operators.append(self.parse_addop())
            terms.append(self.parse_term())
        return Addition(terms, operators)
        
    def parse_addop(self):
        """
        Parses the addop lexem.
        """
        if self.peek().tag == LexemTag.ADDITION:
            self.expect(LexemTag.ADDITION)
            return AddOp(AddOp.ADD)
        elif self.peek().tag == LexemTag.SUBTRACTION:
            self.expect(LexemTag.SUBTRACTION)
            return AddOp(AddOp.SUB)
        else:
            raise ValueError("{} is not a valid addition operator.".format(self.peek()))

    def parse_term(self):
        """
        Parses the term lexem.
        
        The term has the syntax: "Factor { MulOp Factor }"
        """
        factors = []
        operators = []
        factors.append(self.parse_factor())
        while self.peek().tag in [LexemTag.MULTIPLICATION, LexemTag.DIVISION, LexemTag.MODULO]:
            operators.append(self.parse_mulop())
            factors.append(self.parse_factor())
        return Term(factors, operators)
    
    def parse_mulop(self):
        """
        Parses the mulop lexem.
        """
        if self.peek().tag == LexemTag.MULTIPLICATION:
            self.expect(LexemTag.MULTIPLICATION)
            return MulOp(MulOp.MUL)
        elif self.peek().tag == LexemTag.DIVISION:
            self.expect(LexemTag.DIVISION)
            return MulOp(MulOp.DIV)
        elif self.peek().tag == LexemTag.MODULO:
            self.expect(LexemTag.MODULO)
            return MulOp(MulOp.MOD)
        else:
            raise ValueError("{} is not a valid multiplication operator.".format(self.peek()))

    def parse_factor(self):
        """
        Parses the factor lexem.

        The factor has the syntax: "[ UnaryOp ] Primary"
        """
        if self.peek().tag == LexemTag.SUBTRACTION or self.peek().tag == LexemTag.NOT:
            unary_op = self.parse_unary_op()
            primary = self.parse_primary()
            return Factor(primary, unary_op)
        primary = self.parse_primary()
        return Factor(primary, None)

    def parse_unary_op(self):
        """
        Parses the unary op lexem.
        """
        if self.peek().tag == LexemTag.SUBTRACTION:
            self.expect(LexemTag.SUBTRACTION)
            return UnaryOp(UnaryOp.NEG)
        elif self.peek().tag == LexemTag.NOT:
            self.expect(LexemTag.NOT)
            return UnaryOp(UnaryOp.INV)
        else:
            raise ValueError("{} is not a valid unary operator.".format(self.peek()))

    def parse_primary(self):
        """
        Parses the primary lexem.

        The primary has the syntax: "Identifier | Literal"
        """
        if self.peek().tag == LexemTag.IDENTIFIER:
            return Primary(self.parse_identifier())
        elif self.peek().tag in [LexemTag.INTEGER, LexemTag.FLOAT, LexemTag.CHAR, LexemTag.BOOL]:
            return Primary(self.parse_literal())
        else:
            raise ValueError("{} is not a valid primary.".format(self.peek()))

    def parse_literal(self):
        """
        Parses the literal lexem.
        """
        if self.peek().tag == LexemTag.INTEGER:
            return Int(self.expect(LexemTag.INTEGER).value)
        elif self.peek().tag == LexemTag.FLOAT:
            return Float(self.expect(LexemTag.FLOAT).value)
        elif self.peek().tag == LexemTag.CHAR:
            return Char(self.expect(LexemTag.CHAR).value)
        elif self.peek().tag == LexemTag.BOOL:
            return Boolean(self.expect(LexemTag.BOOL).value)
        else:
            raise ValueError("{} is not a valid literal.".format(self.peek()))


