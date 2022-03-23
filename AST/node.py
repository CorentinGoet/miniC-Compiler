"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from abc import ABC, abstractmethod


class Node(ABC):
    """
    Abstract class for the AST nodes.
    -------------
    All children class must implement the accept method for the Visitor Pattern.
    """

    @abstractmethod
    def accept(self, visitor):
        """
        This method accepts the given visitor.
        :param visitor: visitor of the AST
        """


