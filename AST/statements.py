"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Statements(Node):
    """
    Class representation of the Statements node.

    The Statements node has the following syntax:

    Statements = {Statement}
    """

    def __init__(self, statements: list = None):
        """
        Constructor for the Statements node.
        :param statements: list of Statement nodes
        """
        self.statements = statements

    def __str__(self):
        s = "{\n"
        for statement in self.statements:
            s += "\t\t" + str(statement) + "\n"
        s += "\t}"
        return s

    def accept(self, visitor):
        visitor.visitStatements()

