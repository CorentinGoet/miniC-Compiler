"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Block(Node):
    """
    Class representation for the Block node.

    The Block node has the following syntax:

    Block = {Statements}
    """

    def __init__(self, statements: list = None):
        """
        Constructor for the Block node.

        :param statements: list of Statements nodes
        """
        self.statements = statements

    def accept(self, visitor):
        visitor.visitBlock(self)

    def get_statements(self):
        return self.statements

