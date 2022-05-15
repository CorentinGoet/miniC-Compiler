"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
This file contains the enumerations of operators.
"""

import enum
from AST.node import Node


class AddOp(Node, enum.Enum):
    """
    Enumeration of addition operators:

    ADD: +
    SUB: -
    """

    def accept(self, visitor):
        return visitor.visit(self)

    ADD = 1
    SUB = 2


class EquOp(Node, enum.Enum):
    """
    Enumeration of the equality operators.
    equal: ==
    unequal: !=
    """

    def accept(self, visitor):
        return visitor.visit(self)

    equal = 1
    unequal = 2


class UnaryOp(enum.Enum):
    """
    Enumeration of Unary operators

    Unary operators have the following syntax:

    UnaryOp = - | !
    """

    def accept(self, visitor):
        return visitor.visit(self)

    NEG = 1
    INV = 2


class RelOp(enum.Enum):
    """
    Relation Operators enumeration
    INF: <
    SUP: >
    SUPEQ: >=
    INFEQ: <=
    """

    def accept(self, visitor):
        return visitor.visit(self)

    INF = 1
    SUP = 2
    SUPEQ = 3
    INFEQ = 4


class MulOp(enum.Enum):
    """
    Enumeration of multiplication operators

    Multiplication operators have the following syntax:

    MulOp = * | / | %
    """

    def accept(self, visitor):
        return visitor.visit(self)

    MUL = 1
    DIV = 2
    MOD = 3
