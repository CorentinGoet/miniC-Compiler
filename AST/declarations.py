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

    def __str__(self):
        s = "{\n"
        for declaration in self.declarations:
            s += "\t\t\t" + str(declaration) + "\n"
        s += "\t}"
        return s

    def __eq__(self, other):
        if isinstance(other, Declarations):
            return self.declarations == other.declarations
        return False

    def accept(self, visitor):
        visitor.visitDeclarations()
