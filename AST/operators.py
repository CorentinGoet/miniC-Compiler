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
        return visitor.visitOperator(self)

    ADD = "+"
    SUB = "-"


class EquOp(Node, enum.Enum):
    """
    Enumeration of the equality operators.
    equal: ==
    unequal: !=
    """

    def accept(self, visitor):
        return visitor.visitOperator(self)

    equal = "=="
    unequal = "!="


class UnaryOp(enum.Enum):
    """
    Enumeration of Unary operators

    Unary operators have the following syntax:

    UnaryOp = - | !
    """

    def accept(self, visitor):
        return visitor.visitOperator(self)

    NEG = "-"
    INV = "!"


class RelOp(enum.Enum):
    """
    Relation Operators enumeration
    INF: <
    SUP: >
    SUPEQ: >=
    INFEQ: <=
    """

    def accept(self, visitor):
        return visitor.visitOperator(self)

    INF = "<"
    SUP = ">"
    SUPEQ = ">="
    INFEQ = "<="


class MulOp(enum.Enum):
    """
    Enumeration of multiplication operators

    Multiplication operators have the following syntax:

    MulOp = * | / | %
    """

    def accept(self, visitor):
        return visitor.visitOperator(self)

    MUL = "*"
    DIV = "/"
    MOD = "%"
