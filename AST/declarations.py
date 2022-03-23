"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Declarations(Node):
    """
    Class representation for the Declaration nodes.

    Declarations node has the following syntax:

    Declarations = {Declarations}
    """

    def __init__(self, declarations: list = None):
        """
        Constructor for class Declarations
        :param declarations: list of Declaration Node
        """
        self.declarations = declarations

    def accept(self, visitor):
        visitor.visitDeclarations()
