"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import enum


class Lexem:
    """
    The lexem is the token of code containing a value, a type and a position in the source code.
    """
    def __init__(self, value: str, tag: str, position: list):
        self.value = value
        self.tag = tag
        self.position = position

    def __str__(self):
        return "Lexem(value: {}, type: {}, position: {})".format(self.value, self.tag, self.position)

    def __repr__(self):
        return self.tag

    def __eq__(self, other):
        return self.value == other.value and self.tag == other.tag and self.position == other.position


class LexemTag(str, enum.Enum):
    """
    Enumeration of the different possible tags for Lexem.
    """
    MAIN = "MAIN"
    L_PARENTHESIS = "L_PARENTHESIS"
    R_PARENTHESIS = "R_PARENTHESIS"
    L_BRACKET = "L_BRACKET"
    R_BRACKET = "R_BRACKET"
    L_BRACE = "L_BRACE"
    R_BRACE = "R_BRACE"
    TERMINATOR = "TERMINATOR"
    ASSIGNMENT = "ASSIGNMENT"
    ADDITION = "ADDITION"
    SUBTRACTION = "SUBTRACTION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    MODULO = "MODULO"
    TYPE = "TYPE"
    IDENTIFIER = "IDENTIFIER"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    CHAR = "CHAR"
    BOOL = "BOOL"
    IF_kw = "IF"
    ELSE_kw = "ELSE"
    WHILE_kw = "WHILE"
    AND = "AND"
    OR = "OR"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    GREATER = "GREATER"
    LESS = "LESS"
    GREATER_EQUAL = "GREATER_EQUAL"
    LESS_EQUAL = "LESS_EQUAL"
    NOT = "NOT"
    COMMA = "COMMA"

    def __eq__(self, other):
        return self.value == other.value


