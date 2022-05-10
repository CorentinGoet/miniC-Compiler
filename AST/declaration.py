"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.type import Type
from AST.identifier import Identifier



class Declaration(Node):
    """
    Class representation for the Declaration node.

    Declaration node has the following syntax:

    Declaration = Type Identifier [ [Integer] ] {, Identifier [ [Integer] ]};
    """

    def __init__(self, type: Type = None, identifier: list = None, integer: int = None):
        """
        Constructor for the Declaration node.
        :param type: Type node of the declaration
        :param identifier: Identifier node
        :param integer: Integer node (optional: only used for arrays)
        """
        # TODO: add arrays
        self.type = type
        self.identifier = identifier
        self.integer = integer

    def __str__(self):
        return "Declaration : " + str(self.type) + "," + str(self.identifier)

    def __eq__(self, other):
        if isinstance(other, Declaration):
            return self.type == other.type and self.identifier == other.identifier
        return False

    def accept(self, visitor):
        visitor.visitDeclaration(self)

