"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Primary(Node):
    """
    Class representation for the Primary node.

    Primary node has the following syntax:

    Primary = Identifier [ [Expression] ] | Literal | ( Expression ) | Type (Expression)
    """

    def __init__(self, sonNode):
        """
        Constructor for the primary node.

        :param sonNode: Identifier or Literal or (Expression) or Type + Expression
        """
        self.sonNode = sonNode

    def __str__(self):
        return "Primary(" + str(self.sonNode) + ")"

    def accept(self, visitor):
        visitor.visitPrimary()


