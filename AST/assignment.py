"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.identifier import Identifier
from AST.expression import Expression


class Assignment(Node):
    """
    Class representation for the Assignment node.

    The Assignment node syntax is the following:

    Assignment = Identifier [ [Expression] ] = Expression;
    """
    # TODO: add array support

    def __init__(self, identifier: Identifier = None, expression: Expression = None):
        """
        Constructor for the Assignment node.

        :param identifier: Identifier node
        :param expression: Expression node
        """
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return "Assignment: " + str(self.identifier) + " = " + str(self.expression)

    def __eq__(self, other):
        return isinstance(other, Assignment) and self.identifier == other.identifier \
               and self.expression == other.expression

    def accept(self, visitor):
        visitor.visitAssignment()
