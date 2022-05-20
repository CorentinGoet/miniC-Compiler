"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
This file contains the enumerations of operators.
"""

import enum
from AST.node import Node


class Operator(Node, str, enum.Enum):
    """
    Abstract class for operators.
    """

    def __str__(self):
        return self.value

    def accept(self, visitor):
        return visitor.visitOperator(self)


class AddOp(Operator):
    """
    Enumeration of addition operators:

    ADD: +
    SUB: -
    """

    ADD = "+"
    SUB = "-"


class EquOp(Operator):
    """
    Enumeration of the equality operators.
    equal: ==
    unequal: !=
    """

    equal = "=="
    unequal = "!="


class UnaryOp(Operator):
    """
    Enumeration of Unary operators

    Unary operators have the following syntax:

    UnaryOp = - | !
    """

    NEG = "-"
    INV = "!"


class RelOp(Operator):
    """
    Relation Operators enumeration
    INF: <
    SUP: >
    SUPEQ: >=
    INFEQ: <=
    """

    INF = "<"
    SUP = ">"
    SUPEQ = ">="
    INFEQ = "<="


class MulOp(Operator):
    """
    Enumeration of multiplication operators

    Multiplication operators have the following syntax:

    MulOp = * | / | %
    """

    MUL = "*"
    DIV = "/"
    MOD = "%"
