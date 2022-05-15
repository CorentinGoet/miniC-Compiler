"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from abc import ABC, abstractmethod


class Node:
    """
    Abstract class for the AST nodes.
    -------------
    All children class must implement the accept method for the Visitor Pattern.
    """

    def __init__(self, children=None):
        """
        Constructor of the AST node.
        """
        pass

    def accept(self, visitor):
        """
        This method accepts the given visitor.
        :param visitor: visitor of the AST
        """
        raise NotImplementedError

