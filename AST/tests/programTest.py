"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import unittest
from AST.program import Program
from AST.node import Node


class ProgramTest(unittest.TestCase):
    """
    Unit test class for the Program node.
    """

    def testInstantiation(self):
        prog = Program()
        self.assertIsInstance(prog, Program)
        self.assertIsInstance(prog, Node)

