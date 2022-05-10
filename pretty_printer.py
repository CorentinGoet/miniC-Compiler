"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from visitor import Visitor


class PrettyPrinter(Visitor):
    """
    PrettyPrinter class based on the Visitor pattern.

    The pretty printer visits the AST to print the given source code with the correct indentation and formatting.
    """

    def __init__(self):
        """
        Constructor for PrettyPrinter class.
        """
        pass

    def visit(self):
        """
        Visit the AST to print the source code.
        """
        pass


if __name__ == '__main__':
    pass
