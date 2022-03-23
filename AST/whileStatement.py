"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.expression import Expression
from AST.statement import Statement


class WhileStatement(Node):
    """
    Class representation of the While Statement node.

    The while statement has the following syntax:

    WhileStatement = while (Expression) Statement
    """

    def __init__(self, expression: Expression = None, statement: Statement = None):
        """
        Constructor for the while statement node.

        :param expression: Condition  statement of the loop
        :param statement: Statement node
        """
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        visitor.visitWhileStatement()

