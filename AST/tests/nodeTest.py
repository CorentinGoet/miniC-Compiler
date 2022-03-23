"""
@author Corentin Goetghebeur (github.com/CorentinGoet).
Unit test class for the Node class.
"""

import unittest
from AST.node import Node


class MyTestCase(unittest.TestCase):
    """
    Unit test class for the Node class.
    """
    def test_abstract(self):
        """
        Check that the class is abstract.
        """
        self.assertRaises(TypeError, Node)



if __name__ == '__main__':
    unittest.main()
