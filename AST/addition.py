"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Addition(Node):
    """
    Class representation for the Addition node.

    The addition node has the following syntax:

    Addition = Term { AddOp Term }
    """

    def __init__(self, terms: list = None, operators: list = None):
        """
        Constructor for the Addition node.
        :param terms: list of Term nodes (of length N)
        :param operators: list of addition operators (AddOp) of length N-1
        """
        self.terms = terms
        self.operators = operators

    def __str__(self):
        s = "Addition("
        for i in range(len(self.terms)):
            s += str(self.terms[i])
            if self.operators is not None and i < len(self.operators):
                s += str(self.operators[i])
        s += ")"
        return s

    def accept(self, visitor):
        visitor.visitAddition(self)

    def get_terms(self):
        return self.terms

    def get_operators(self):
        return self.operators

