"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from AST.node import Node
from AST.expression import Expression
from AST.statement import Statement


class IfStatement(Node):
    """
    Class representation for the If Statement node.

    The IfStatement node has the following syntax:

    IfStatement = if (Expression) Statement [else Statement]
    """

    def __init__(self, expression: Expression = None, trueStatement: Statement = None, falseStatement: Statement =None):
        """
        Constructor for the If statement node.

        :param expression: condition Expression
        :param trueStatement: Statement executed if the expression is true
        :param falseStatement: Statement executed if the expression is false
        """
        self.expression = expression
        self.trueStatement = trueStatement
        self.falseStatement = falseStatement

    def accept(self, visitor):
        visitor.visitIfStatement()

