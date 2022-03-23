"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.addition import Addition
import enum


class Relation(Node):
    """
    Class representation of the Relation node.

    Relation node has the following syntax:

    Relation = Addition [ RelOp Addition]
    """

    def __init__(self, addition1: Addition = None, relOp: RelOp = None, addition2: Addition= None):
        """
        Constructor for the Relation node.

        :param addition1: first Addition node
        :param relOp: relation operator ( >, <, <= or >=)
        :param addition2: second Addition node
        """
        self.addition1 = addition1
        self.relOp = relOp
        self.addition2 = addition2

    def accept(self, visitor):
        visitor.visitRelation()


class RelOp(enum):
    """
    Relation Operators enumeration
    INF: <
    SUP: >
    SUPEQ: >=
    INFEQ: <=
    """
    INF = 1
    SUP = 2
    SUPEQ = 3
    INFEQ = 4