"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node


class Statement(Node):
    """
    Class representation for the Statement node.

    The Statement node has the following syntax:

    Statement = ; | Block | Assignment | IfStatement | WhileStatement
    """

    def __init__(self, son_node):
        """
        Constructor for the Statement node.
        :param son_node: either a separator, a block, an assignment, an IfStatement or a WhileStatement.
        """
        self.son_node = son_node

    def accept(self, visitor):
        visitor.visitStatement()


