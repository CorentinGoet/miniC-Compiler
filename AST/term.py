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
        self.factors = factors
        self.operators = operators

    def __str__(self):
        s = "Term("
        for i in range(len(self.factors)):
            s += str(self.factors[i])
            if i < len(self.operators):
                s += str(self.operators[i])
        s += ")"
        return s

    def accept(self, visitor):
        visitor.visitTerm(self)

    def get_factors(self):
        return self.factors

    def get_operators(self):
        return self.operators



