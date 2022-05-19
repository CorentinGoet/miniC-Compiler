import unittest
from lexer import Lexer
from parser.parser import Parser
from pretty_printer import PrettyPrinter


class MyTestCase(unittest.TestCase):

    def testTest(self):
        source = "int main() { int a; a = 1;}"
        lexer = Lexer()
        lexer.tokenize(source)
        parser = Parser()
        parser.parse(lexer.lexems)
        prettyPrinter = PrettyPrinter()
        prettyPrinter.visit(parser.ast)
        print(prettyPrinter.clean_source)


if __name__ == '__main__':
    unittest.main()
