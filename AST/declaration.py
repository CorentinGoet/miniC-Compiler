"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.type import Type
from AST.identifier import Identifier
from AST.Integer import Integer


class Declaration(Node):
    """
    Class representation for the Declaration node.

    Declaration node has the following syntax:

    Declaration = Type Identifier [ [Integer] ] {, Identifier [ [Integer] ]};
    """

    def __init__(self, type: Type = None, identifier: Identifier = None, integer: Integer = None):
        """
        Constructor for the Declaration node.
        :param type: Type node of the declaration
        :param identifier: Identifier node
        :param integer: Integer node (optional: only used for arrays)
        """
        # TODO: add arrays
        self.identifier = identifier
        self.integer = integer

    def accept(self, visitor):
        visitor.visitDeclaration()
