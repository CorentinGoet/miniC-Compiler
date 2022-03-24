"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
import enum


class Term(Node):
    """
    Class representation for the Term node.

    The term node has the following syntax:

    Term = Factor { MulOp Factor }
    """

    def __init__(self, factors: list = None, operators: list = None):
        """
        Constructor for the Term node.

        :param factors: list of Factor node
        :param operators: list of multiplication operators (MulOp)
        """

    def accept(self, visitor):
        visitor.visitTerm()


class MulOp(enum):
    """
    Enumeration of multiplication operators

    Multiplication operators have the following syntax:

    MulOp = * | / | %
    """
    MUL = 1
    DIV = 2
    MOD = 3

