"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
import enum


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

    def accept(self, visitor):
        visitor.visitAddition()


class AddOp(enum):
    """
    Enumeration of addition operators:
    ADD: +
    SUB: -
    """
    ADD = 1
    SUB = 2