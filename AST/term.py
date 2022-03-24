"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


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




