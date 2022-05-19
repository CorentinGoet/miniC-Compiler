import unittest
from lexer_pkg.lexer import Lexer
from parser_pkg.parser import Parser
from pretty_printer import PrettyPrinter


class PrettyPrintertest(unittest.TestCase):

    def testTest(self):
        source = "int main() { int a; a = 1;}"
        lexer = Lexer()
        lexer.tokenize(source)
        parser = Parser()
        parser.parse(lexer.lexems)
        prettyPrinter = PrettyPrinter()
        print(parser.ast)
        prettyPrinter.visit(parser.ast)
        print(prettyPrinter.clean_source)


if __name__ == '__main__':
    unittest.main()
