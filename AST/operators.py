"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
This file contains the enumerations of operators.
"""

import enum


class AddOp(enum.Enum):
    """
    Enumeration of addition operators:

    ADD: +
    SUB: -
    """
    ADD = 1
    SUB = 2


class EquOp(enum.Enum):
    """
    Enumeration of the equality operators.
    equal: ==
    unequal: !=
    """
    equal = 1
    unequal = 2


class UnaryOp(enum.Enum):
    """
    Enumeration of Unary operators

    Unary operators have the following syntax:

    UnaryOp = - | !
    """
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
    MUL = 1
    DIV = 2
    MOD = 3