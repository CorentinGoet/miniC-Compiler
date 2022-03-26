"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import enum
from AST.node import Node
from AST.relation import Relation
from AST.operators import EquOp


class Equality(Node):
    """
    Class representation for the Equality node.

    The Equality node has the following syntax:

    Equality = Relation [ EquOp Relation ]
    """

    def __init__(self, relation1: Relation = None, equOp: EquOp = None, relation2: Relation = None):
        """
        Constructor for the equality node.

        :param relation1: Relation node
        :param equOp: EquOp node (== or !=)
        :param relation2: Relation node
        """
        self.relation1 = relation1
        self.equOp = equOp
        self.relation2 = relation2

    def __str__(self):
        return "Equality({}, {}, {})".format(self.relation1, self.equOp, self.relation2)

    def accept(self, visitor):
        visitor.visitEquality()



