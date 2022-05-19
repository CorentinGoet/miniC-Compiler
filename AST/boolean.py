"""
@author CorentinGoet
"""

from AST.node import Node


class Boolean(Node):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Boolean({})".format(self.value)

    def accept(self, visitor):
        return visitor.visitBoolean(self)

