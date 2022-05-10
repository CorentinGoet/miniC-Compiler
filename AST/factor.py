"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.primary import Primary
from AST.operators import UnaryOp


class Factor(Node):
    """
    Class representation for the Factor node.

    The Factor node has the following syntax:

    Factor = [ UnaryOp ] Primary
    """

    def __init__(self, primary: Primary = None, unaryOp: UnaryOp = None):
        """
        Constructor for the Factor node.

        :param primary: primary node
        :param unaryOp: unary operator
        """
        self.primary = primary
        self.unaryOp = unaryOp

    def __str__(self):
        s = "Factor("
        if self.unaryOp is not None:
            s += str(self.unaryOp) + " "
        s += str(self.primary)
        s += ")"
        return s

    def accept(self, visitor):
        visitor.visitFactor(self)


