"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Conjunction(Node):
    """
    Class representation for the conjunction node.

    The conjunction node has the following syntax:

    Conjunction = Equality {&& Equality}
    """

    def __init__(self, equalities: list = None):
        """
        Constructor for the Conjunction node.

        :param equalities: list of Equality nodes
        """
        self.equalities = equalities

    def __str__(self):
        s = "Conjunction { "
        for equality in self.equalities:
            s += str(equality) + " "
        s += "}"
        return s

    def accept(self, visitor):
        visitor.visitConjunction(self)

    def get_equalities(self):
        return self.equalities

