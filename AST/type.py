"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
import enum


class Type(Node):
    """
    Class representation of the Type node.

    The Type node has the following syntax.

    Type = int | bool | float | char

    Use Types.[INT | BOOL | FLOAT | CHAR] to instantiate].
    """

    def __init__(self, type: int):
        """
        Constructor for Type node.

        Use the Types enumeration for parameter type.

        Example:

        t = Type(Types.INT)

        :param type: Types element from enumeration.
        """
        self.type = type

    def accept(self, visitor):
        visitor.visitType()


class Types(enum.Enum):
    """
    Type enumeration.
    """
    INT = "int"
    BOOL = "bool"
    FLOAT = "float"
    CHAR = "char"
