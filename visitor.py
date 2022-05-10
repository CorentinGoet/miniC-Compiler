"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""


class Visitor:
    """
    Visitor abstract class
    """

    def visit(self, element):
        """
        Visit an element
        """
        raise NotImplementedError

