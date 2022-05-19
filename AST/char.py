"""
@author CorentinGoet
"""

from AST.node import Node


class Char(Node):

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value

    def accept(self, visitor):
        visitor.visitChar(self)

