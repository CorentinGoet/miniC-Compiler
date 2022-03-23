"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import unittest
from AST.declarations import Declarations
from AST.node import Node


class DeclarationsTest(unittest.TestCase):
    """
    Test class for Declarations node.
    """

    def testInstantiation(self):
        dec = Declarations()
        self.assertIsInstance(dec, Declarations)
        self.assertIsInstance(dec, Node)


if __name__ == '__main__':
    unittest.main()
