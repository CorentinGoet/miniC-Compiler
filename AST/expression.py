"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Expression(Node):
    """
    Class representation for the expression node.

    The expression node has the following syntax:

    Expression = Conjunction {|| Conjunction}
    """

    def __init__(self, conjunctions: list = None):
        """
        Constructor for the Expression node.

        :param conjunctions: list of Conjunction nodes
        """
        self.conjunctions = conjunctions

    def __str__(self):
        s = "Expression : {"
        for conjunction in self.conjunctions:
            s += " " + str(conjunction)
        s += "}"
        return s

    def accept(self, visitor):
        visitor.visitExpression()
