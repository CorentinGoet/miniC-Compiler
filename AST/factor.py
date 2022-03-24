"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.primary import Primary
import enum


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

    def accept(self, visitor):
        visitor.visitFactor()


class UnaryOp(enum):
    """
    Enumeration of Unary operators

    Unary operators have the following syntax:

    UnaryOp = - | !
    """
    NEG = 1
    INV = 2
