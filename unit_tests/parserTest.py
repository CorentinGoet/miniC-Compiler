"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import unittest

from AST import *
from parser import Parser
from lexem import Lexem, LexemTag
from lexer import Lexer


class ParserTest(unittest.TestCase):
    """
    Test class for the parser.
    """

    def setUp(self):
        """
        Set up the test.
        """
        self.parser = Parser()
        self.lexer = Lexer()

    def testPeek(self):
        """
        Test the peek function.
        """
        lexem = Lexem("123", LexemTag.INTEGER, [1, 0])
        self.parser.lexems = [lexem]
        self.assertEqual(self.parser.peek(), lexem)
        self.parser.lexems = []
        self.assertRaises(ValueError, self.parser.peek)

    def testExpectAccept(self):
        """
        Test the expect function.
        """
        lexem = Lexem("123", LexemTag.INTEGER, [1, 0])
        self.parser.lexems = [lexem]
        self.assertEqual(self.parser.expect(LexemTag.INTEGER), lexem)
        self.assertEqual(self.parser.lexems, [])
        self.parser.lexems = [lexem]
        self.assertRaises(TypeError, self.parser.expect, LexemTag.CHAR)

    def test_parse_program(self):
        """
        Test the parse_program function.
        """
        f = open("test_sources/test_program.minic", "r")
        source_code = f.read()
        f.close()
        self.lexer.tokenize(source_code)
        self.parser.parse(self.lexer.lexems)
        self.assertEqual(self.parser.lexems, [])
        self.assertEqual(self.parser.ast, Program(Declarations([]), Statements([])))

    def test_parse_declarations(self):
        """
        Test the parse_declarations function.
        """
        f = open("test_sources/test_declarations.minic", "r")
        source_code = f.read()
        f.close()
        self.lexer.tokenize(source_code)
        self.parser.parse(self.lexer.lexems)
        self.assertEqual(self.parser.lexems, [])
        declarations = Declarations([Declaration(Type(Types.INT), [Identifier("a")]),
                                     Declaration(Type(Types.INT), [Identifier("bTest2Var"), Identifier("c")]),
                                     Declaration(Type(Types.FLOAT), [Identifier("d")]),
                                     Declaration(Type(Types.FLOAT), [Identifier("e"), Identifier("f2Test")]),
                                     Declaration(Type(Types.CHAR), [Identifier("h")]),
                                     Declaration(Type(Types.CHAR), [Identifier("i"), Identifier("jTestVar")]),
                                     Declaration(Type(Types.BOOL), [Identifier("aTestVar")]),
                                     Declaration(Type(Types.BOOL), [Identifier("b"), Identifier("cTest2Var")])])
        self.assertEqual(self.parser.ast.declarations, declarations)

        # Test the parse_declarations function with a wrong declaration
        f = open("test_sources/test_declaration_error.minic", "r")
        source_code = f.read()
        f.close()
        self.lexer.tokenize(source_code)
        self.assertRaises(TypeError, self.parser.parse, self.lexer.lexems)

    def test_parse_assignment(self):
        """
        Test the parse_assignment function.
        """
        f = open("test_sources/test_assignment.minic", "r")
        source_code = f.read()
        f.close()
        self.lexer.tokenize(source_code)
        self.parser.parse(self.lexer.lexems)
        self.assertEqual(self.parser.lexems, [])

    def test_parse_if(self):
        """
        Test the parse_ifStatement function.
        """
        f = open("test_sources/test_ifStatement.minic", "r")
        source_code = f.read()
        f.close()
        self.lexer.tokenize(source_code)
        self.parser.parse(self.lexer.lexems)

    def test_parse_while(self):
        """
        Test the parse_whileStatement function.
        """
        f = open("test_sources/test_whileStatement.minic", "r")
        source_code = f.read()
        f.close()
        self.lexer.tokenize(source_code)
        self.parser.parse(self.lexer.lexems)
        self.assertEqual(self.parser.lexems, [])

    def test_parse_operators(self):
        """
        Test the parsing of operators.
        """
        f = open("test_sources/test_operators.minic", "r")
        source_code = f.read()
        f.close()
        self.lexer.tokenize(source_code)
        self.parser.parse(self.lexer.lexems)
        self.assertEqual(self.parser.lexems, [])

        # test operator errors
        f = open("test_sources/test_operator_error.minic", "r")
        source_code = f.read()
        f.close()
        self.lexer.tokenize(source_code)
        self.assertRaises(TypeError, self.parser.parse, self.lexer.lexems)




if __name__ == '__main__':
    unittest.main()
