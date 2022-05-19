"""
@author CorentinGoet
"""

from AST.node import Node


class Int(Node):

    def accept(self, visitor):
        visitor.visitInt(self)

    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return str(self.value)
