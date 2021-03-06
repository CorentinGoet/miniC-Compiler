"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Identifier(Node):
    """
    Class representation for the Identifier node.

    Identifier has the following syntax:

    Identifier = Letter{ Letter | Digit }
    """

    def __init__(self, name: str = None):
        """
        Constructor for the Identifier node.

        :param name: name of the declared value.
        """
        self.name = name

    def __str__(self):
        return "Identifier: " + self.name

    def __eq__(self, other):
        return isinstance(other, Identifier) and self.name == other.name

    def accept(self, visitor):
        visitor.visitIdentifier(self)


