"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""
import sys
from lexem import LexemTag
from AST import *


class Parser:
    """
    The parser takes the lexems from the lexer and builds the AST.
    """

    def __init__(self):
        self.lexems = []


    def peek(self, n: int=0):
        """
        Returns the nth next lexem without consuming it.
        """
        if len(self.lexems) > n:
            return self.lexems[n]
        else:
            print("Error: no more lexems to peek.")
            sys.exit(1)

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
                break
        return Declarations(declarations)

    def parse_declaration(self):
        """
        Parses the declaration lexem.

        The declaration has the syntax "type id;"
        """
        type = self.parse_type()
        id = self.parse_identifier()
        self.expect(LexemTag.TERMINATOR)
        return Declaration(type, id)

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

    def parse_block(self):
        """
        Parses the block lexem.
        """
        pass

    def parse_statements(self):
        """
        Parses the statements lexem.
        """
        pass

    def parse_statement(self):
        """
        Parses the statement lexem.
        """
        pass

    def parse_expression(self):
        """
        Parses the expression lexem.
        """
        pass

    def parse_assignment(self):
        """
        Parses the assignment lexem.
        """
        pass

    def parse_ifStatement(self):
        """
        Parses the ifStatement lexem.
        """
        pass

    def parse_whileStatement(self):
        """
        Parses the whileStatement lexem.
        """
        pass

    def parse_conjunction(self):
        """
        Parses the conjunction lexem.
        """
        pass

    def parse_equality(self):
        """
        Parses the equality lexem.
        """
        pass

    def parse_equop(self):
        """
        Parses the equop lexem.
        """
        pass

    def parse_relop(self):
        """
        Parses the relop lexem.
        """
        pass

    def parse_addop(self):
        """
        Parses the addop lexem.
        """
        pass

    def parse_relation(self):
        """
        Parses the relation lexem.
        """
        pass

    def parse_term(self):
        """
        Parses the term lexem.
        """
        pass

    def parse_factor(self):
        """
        Parses the factor lexem.
        """
        pass


