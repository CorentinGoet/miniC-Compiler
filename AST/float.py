"""
@author CorentinGoet
"""

from AST.node import Node


class Float(Node):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def accept(self, visitor):
        visitor.visitFloat(self)
