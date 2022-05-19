"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import unittest
from lexer_pkg.lexer import Lexer
from lexer_pkg.lexem import Lexem, LexemTag


class testLexer(unittest.TestCase):
    """
    Test class for the Lexer.

    Each different syntax will be tested in a separate method.
    """
    def setUp(self) -> None:
        """
        Initialize the lexer.
        (This method is called before each test.)
        """
        self.lexer = Lexer()

    def test_lexem(self):
        """
        Tests the methods inside of the Lexem class.
        """
        lexem = Lexem("42", LexemTag.INTEGER, [2, 3])
        self.assertEqual(lexem.tag, LexemTag.INTEGER)
        self.assertEqual(lexem.value, "42")
        self.assertEqual(lexem.position, [2, 3])
        test_lexem = Lexem("42", LexemTag.INTEGER, [2, 3])
        self.assertEqual(test_lexem, lexem)
        self.assertNotEqual(test_lexem, Lexem("42", LexemTag.INTEGER, [2, 4]))
        self.assertNotEqual(test_lexem, Lexem("42", LexemTag.INTEGER, [3, 3]))
        self.assertNotEqual(test_lexem, Lexem("43", LexemTag.INTEGER, [2, 3]))
        self.assertNotEqual(test_lexem, Lexem("42", LexemTag.FLOAT, [2, 3]))
        self.assertEqual("Lexem(value: 42, type: INTEGER, position: [2, 3])", str(test_lexem))

    def test_str_lexer(self):
        """
        Tests the str representation of the lexer.
        """
        source_code = "int a"
        self.lexer.tokenize(source_code)
        self.assertEqual(str(self.lexer), "Lexem(value: int, type: TYPE, position: [1, 0])\nLexem(value: a, type: IDENTIFIER, position: [1, 4])")

    def test_main(self):
        """
        Tests the lexing of the main.
        """
        source_code = "main"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("main", LexemTag.MAIN, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)

    def test_parenthesis(self):
        """
        Tests the lexer for the parenthesis.
        """
        source_code = "()"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("(", LexemTag.L_PARENTHESIS, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem(")", LexemTag.R_PARENTHESIS, [1, 1])
        self.assertEqual(self.lexer.lexems[1], ref_token)

    def test_brackets(self):
        """
        Tests the lexer for the brackets.
        """
        source_code = "[]"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("[", LexemTag.L_BRACKET, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem("]", LexemTag.R_BRACKET, [1, 1])
        self.assertEqual(self.lexer.lexems[1], ref_token)

    def test_braces(self):
        """
        Tests the lexer for the braces.
        """
        source_code = "{}"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("{", LexemTag.L_BRACE, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem("}", LexemTag.R_BRACE, [1, 1])
        self.assertEqual(self.lexer.lexems[1], ref_token)

    def test_operators(self):
        """
        Tests the lexer for the operators "+", "-", "/", "*" and "%"
        """
        source_code = "+-*/%"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("+", LexemTag.ADDITION, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem("-", LexemTag.SUBTRACTION, [1, 1])
        self.assertEqual(self.lexer.lexems[1], ref_token)
        ref_token = Lexem("*", LexemTag.MULTIPLICATION, [1, 2])
        self.assertEqual(self.lexer.lexems[2], ref_token)
        ref_token = Lexem("/", LexemTag.DIVISION, [1, 3])
        self.assertEqual(self.lexer.lexems[3], ref_token)
        ref_token = Lexem("%", LexemTag.MODULO, [1, 4])
        self.assertEqual(self.lexer.lexems[4], ref_token)

    def test_punctuation(self):
        """
        Tests the lexer for the punctuation ";" and ","
        """
        source_code = ";,"
        self.lexer.tokenize(source_code)
        ref_token = Lexem(";", LexemTag.TERMINATOR, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem(",", LexemTag.COMMA, [1, 1])
        self.assertEqual(self.lexer.lexems[1], ref_token)

    def test_comparison_operators(self):
        """
        Tests the lexer for the operators "==", "!=", "<", ">", "<=" and ">=".
        """
        source_code = "==!=<><=>="
        self.lexer.tokenize(source_code)
        ref_token = Lexem("==", LexemTag.EQUAL, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem("!=", LexemTag.NOT_EQUAL, [1, 2])
        self.assertEqual(self.lexer.lexems[1], ref_token)
        ref_token = Lexem("<", LexemTag.LESS, [1, 4])
        self.assertEqual(self.lexer.lexems[2], ref_token)
        ref_token = Lexem(">", LexemTag.GREATER, [1, 5])
        self.assertEqual(self.lexer.lexems[3], ref_token)
        ref_token = Lexem("<=", LexemTag.LESS_EQUAL, [1, 6])
        self.assertEqual(self.lexer.lexems[4], ref_token)
        ref_token = Lexem(">=", LexemTag.GREATER_EQUAL, [1, 8])
        self.assertEqual(self.lexer.lexems[5], ref_token)

    def test_assignment_operator(self):
        """
        Tests the lexer for the operator "=".
        """
        source_code = "="
        self.lexer.tokenize(source_code)
        ref_token = Lexem("=", LexemTag.ASSIGNMENT, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)

    def test_logic_operators(self):
        """
        Tests the lexer for the operators "&&", "||", "!"
        """
        source_code = "&&||!"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("&&", LexemTag.AND, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem("||", LexemTag.OR, [1, 2])
        self.assertEqual(self.lexer.lexems[1], ref_token)
        ref_token = Lexem("!", LexemTag.NOT, [1, 4])
        self.assertEqual(self.lexer.lexems[2], ref_token)

    def test_keywords(self):
        """
        Tests the lexer for the keywords "if", "else" and "while"
        """
        source_code = "ifelsewhile"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("if", LexemTag.IF_kw, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem("else", LexemTag.ELSE_kw, [1, 2])
        self.assertEqual(self.lexer.lexems[1], ref_token)
        ref_token = Lexem("while", LexemTag.WHILE_kw, [1, 6])
        self.assertEqual(self.lexer.lexems[2], ref_token)

    def test_types(self):
        """
        Tests the lexer for the types "int", "float", "bool" and "char".
        """
        source_code = "intfloatboolchar"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("int", LexemTag.TYPE, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem("float", LexemTag.TYPE, [1, 3])
        self.assertEqual(self.lexer.lexems[1], ref_token)
        ref_token = Lexem("bool", LexemTag.TYPE, [1, 8])
        self.assertEqual(self.lexer.lexems[2], ref_token)
        ref_token = Lexem("char", LexemTag.TYPE, [1, 12])
        self.assertEqual(self.lexer.lexems[3], ref_token)

    def test_booleans(self):
        """
        Tests the lexer for the booleans "true" and "false".
        """
        source_code = "truefalse"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("true", LexemTag.BOOL, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)
        ref_token = Lexem("false", LexemTag.BOOL, [1, 4])
        self.assertEqual(self.lexer.lexems[1], ref_token)

    def test_integer(self):
        """
        Tests the lexer for the integer "123".
        """
        source_code = "123"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("123", LexemTag.INTEGER, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)

    def test_float(self):
        """
        Tests the lexer for the float "123.456".
        """
        source_code = "123.456"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("123.456", LexemTag.FLOAT, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)

    def test_char(self):
        """
        Tests the lexer for the char "'a'".
        """
        source_code = "'a'"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("'a'", LexemTag.CHAR, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)

    def test_identifier(self):
        """
        Tests the lexer for the identifier "abc".
        """
        source_code = "abc"
        self.lexer.tokenize(source_code)
        ref_token = Lexem("abc", LexemTag.IDENTIFIER, [1, 0])
        self.assertEqual(self.lexer.lexems[0], ref_token)

    def test_blanks(self):
        """
        Tests the lexer for the whitespaces, the tabs and the return.
        """
        source_code = " \t\n\r"
        self.lexer.tokenize(source_code)
        self.assertEqual(self.lexer.lexems, [])

    def test_errors(self):
        """
        Tests the lexer for invalid characters.
        """
        source_code = "$"
        self.assertRaises(Exception, self.lexer.tokenize, source_code)


if __name__ == '__main__':
    unittest.main()
