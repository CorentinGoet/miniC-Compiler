"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from visitor import Visitor


class PrettyPrinter(Visitor):
    """
    PrettyPrinter class based on the Visitor pattern.

    The pretty printer visits the AST to print the given source code with the correct indentation and formatting.
    """

    def __init__(self):
        """
        Constructor for PrettyPrinter class.
        """
        self.context = Context()
        self.clean_source = ""

    def visit(self, node):
        """
        Visit the AST to print the source code.
        """
        node.accept(self)
        return self.clean_source

    def visitProgram(self, program):
        """
        Visit and pretty-print the program node.
        :param program: program node
        """
        self.clean_source += "int main() {\n"
        self.context.increase_tabs()
        program.declarations.accept(self)
        self.clean_source += "\n"
        program.statements.accept(self)
        self.context.decrease_tabs()
        self.clean_source += "}\n"

    def visitDeclarations(self, declarations):
        """
        Visit and pretty-print the declarations node.
        :param declarations: declarations node
        """
        for declaration in declarations.declarations:
            self.visitDeclaration(declaration)
            if declaration is not declarations.declarations[-1]:
                self.clean_source += "\n"

    def visitDeclaration(self, declaration):
        """
        Visit and pretty-print the declaration node.
        :param declaration: declaration node
        """
        self.clean_source += self.context.get_tabs() * " "
        declaration.type.accept(self)
        self.clean_source += " "
        declaration.identifier[0].accept(self)
        if len(declaration.identifier) > 1:
            for id in declaration.identifier[1:]:
                self.clean_source += ", "
                id.accept(self)
        self.clean_source += ";\n"

    def visitStatements(self, statements):
        """
        Visit and pretty-print the statements node.
        :param statements: statements node
        """
        for statement in statements.statements:
            self.clean_source += self.context.get_tabs() * " "
            statement.accept(self)
            if statement is not statements.statements[-1]:
                self.clean_source += "\n"

    def visitStatement(self, statement):
        """
        Visit and pretty-print the statement node.
        :param statement: statement node
        """
        statement.son_node.accept(self)

    def visitBlock(self, block):
        """
        Visit and pretty-print the block node.
        :param block: block node
        """
        for statement in block.statements:
            statement.accept(self)

    def visitIfStatement(self, if_statement):
        """
        Visit and pretty-print the if statement node.
        :param if_statement: if statement node
        """
        self.clean_source += self.context.get_tabs() * " " + "if (" + if_statement.expression.accept(self) + ") {\n"
        self.context.increase_tabs()
        self.visit(if_statement.trueStatement.accept(self))
        self.context.decrease_tabs()

        if if_statement.falseStatement is not None:
            self.clean_source += self.context.get_tabs() * " " + "} else {\n"
            self.context.increase_tabs()
            self.visit(if_statement.falseStatement.accept(self))
            self.context.decrease_tabs()

        self.clean_source += self.context.get_tabs() * " " + "}\n"

    def visitWhileStatement(self, while_statement):
        """
        Visit and pretty-print the while statement node.
        :param while_statement: while statement node
        """
        self.clean_source += self.context.get_tabs() * " " + "while (" + while_statement.expression.accept(
            self) + ") {\n"
        self.context.increase_tabs()
        self.visit(while_statement.statement.accept(self))
        self.context.decrease_tabs()
        self.clean_source += self.context.get_tabs() * " " + "}\n"

    def visitExpression(self, expression):
        """
        Visit and pretty-print the expression node.
        :param expression: expression node
        """
        for conjunction in expression.conjunctions:
            conjunction.accept(self)
            if conjunction is not expression.conjunctions[-1]:
                self.clean_source += " && "

    def visitConjunction(self, conjunction):
        """
        Visit and pretty-print the conjunction node.
        :param conjunction: conjunction node
        """
        for disjunction in conjunction.equalities:
            disjunction.accept(self)
            if disjunction is not conjunction.equalities[-1]:
                self.clean_source += " || "

    def visitEquality(self, equality):
        """
        Visit and pretty-print the equality node.
        :param equality: equality node
        """
        equality.relation1.accept(self)
        if equality.relation2 is not None:
            self.clean_source += " "
            equality.equOp.accept(self)
            self.clean_source += " "
            equality.relation2.accept(self)

    def visitRelation(self, relation):
        """
        Visit and pretty-print the relation node.
        :param relation: relation node
        """
        relation.addition1.accept(self)
        self.clean_source += " "
        if relation.relOp is not None:
            relation.relOp.accept(self)
            self.clean_source += " "
            relation.addition2.accept(self)

    def visitAddition(self, addition):
        """
        Visit and pretty-print the addition node.
        :param addition: addition node
        """
        addition.terms[0].accept(self)

        if len(addition.terms) > 1:
            for i in range(1, len(addition.terms)):
                self.clean_source += " " + addition.operators[i].accept(self) + " "
                self.clean_source += addition.terms[i].accept(self)

    def visitTerm(self, term):
        """
        Visit and pretty-print the term node.
        :param term: term node
        """
        term.factors[0].accept(self)
        if len(term.factors) > 1:
            for i in range(1, len(term.factors)):
                self.clean_source += " "
                term.operators[i].accept(self)
                self.clean_source += " "
                term.factors[i].accept(self)

    def visitAssignment(self, assignment):
        """
        Visit and pretty-print the assignment node.
        :param assignment: assignment node
        """
        assignment.identifier.accept(self)
        self.clean_source += " = "
        assignment.expression.accept(self)
        self.clean_source += ";\n"

    def visitFactor(self, factor):
        """
        Visit and pretty-print the factor node.
        :param factor: factor node
        """
        if factor.unaryOp is not None:
            factor.unaryOp.accept(self)

        factor.primary.accept(self)

    def visitPrimary(self, primary):
        """
        Visit and pretty-print the primary node.
        :param primary: primary node
        """
        primary.sonNode.accept(self)

    def visitIdentifier(self, identifier):
        """
        Visit and pretty-print the identifier node.
        :param identifier: identifier node
        """
        self.clean_source += identifier.name

    def visitType(self, type):
        """
        Visit and pretty-print the type node.
        :param type: type node
        """
        self.clean_source += type.type

    def visitLiteral(self, literal):
        """
        Visit and pretty-print the literal node.
        :param literal: literal node
        """
        self.clean_source += literal.name

    def visitType(self, type):
        """
        Visit and pretty-print the type node.
        :param type: type node
        """
        self.clean_source += type.type

    def visitOperator(self, operator):
        """
        Visit and pretty-print the operator node (relOp, addOp, equOp, unaryOp, mulOp).
        :param operator: operator node
        """
        self.clean_source += operator.operator

    def visitInt(self, int):
        """
        Visit and pretty-print the int node.
        :param int: int node
        """
        self.clean_source += str(int.value)

    def visitFloat(self, float):
        """
        Visit and pretty-print the float node.
        :param float: float node
        """
        self.clean_source += str(float.value)

    def visitChar(self, char):
        """
        Visit and pretty-print the char node.
        :param char: char node
        """
        self.clean_source += char.value

    def visitBoolean(self, boolean):
        """
        Visit and pretty-print the boolean node.
        :param boolean: boolean node
        """
        self.clean_source += str(boolean.value)

class Context:
    """
    Class representation of the pretty-printer visitor's current context.
    """

    def __init__(self):
        self.nb_tabs = 0

    def increase_tabs(self):
        self.nb_tabs += 1

    def decrease_tabs(self):
        self.nb_tabs -= 1

    def get_tabs(self):
        return self.nb_tabs




if __name__ == '__main__':
    pass
