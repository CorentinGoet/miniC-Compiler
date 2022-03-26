"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.declarations import Declarations
from AST.statements import Statements


class Program(Node):
    """
    Class representation for the program node on the Abstract Syntax Tree.

    The program has the following syntax:

    Program = int main(){Declarations Statements}
    """

    def __init__(self, declarations: Declarations = None, statements: Statements = None):
        """
        Constructor for the program node.

        :param declarations: Declaration node
        :param statements: Statement node
        """
        self.declarations = declarations
        self.statements = statements

    def __str__(self):
        return "Program(\n\tDeclarations: {}\n\tStatements: {}\n)".format(self.declarations, self.statements)

    def accept(self, visitor):
        visitor.visitProgram()
