"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
import enum


class Literal(Node):
    """
    Class representation for the Literal node.

    The literal node has the following syntax:

    Literal = Integer | Boolean | Float | Char
    """

    def __init__(self, sonNode):
        """
        Constructor for the literal node.

        :param sonNode: Integer or Boolean or Float or Char
        """
        self.sonNode = sonNode

    def accept(self, visitor):
        visitor.visitLiteral(self)


