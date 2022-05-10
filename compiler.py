"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from visitor import Visitor


class Compiler(Visitor):
    """
    Compiler class
    """

    def __init__(self):
        """
        Constructor of the Compiler class
        """

    def visit(self):
        """
        Visit the AST to produce assembly code.
        """
        pass


if __name__ == '__main__':
    pass
