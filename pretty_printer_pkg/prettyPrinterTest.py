import unittest
from lexer_pkg.lexer import Lexer
from parser_pkg.parser import Parser
from pretty_printer import PrettyPrinter


class PrettyPrinterTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lexer = Lexer()
        self.parser = Parser()
        self.prettyPrinter = PrettyPrinter()

    def testDeclarations(self):
        source = "int main() {int a, b, c;char d;float e, f;bool g, h;}"
        f = open("test_resources/prettyDeclarations.minic", "r")
        pretty_source = f.read()
        f.close()

        self.lexer.tokenize(source)
        self.parser.parse(self.lexer.lexems)
        self.prettyPrinter.visit(self.parser.ast)
        self.assertEqual(pretty_source, self.prettyPrinter.clean_source)


    def testVisitIfStatement(self):
        source = 'int main() {int a, b;if (a == b) {c = d;} else {d = e;}}'

        f = open('test_resources/prettyIfStatement.minic', 'r')
        pretty_source = f.read()
        f.close()

        self.lexer.tokenize(source)
        self.parser.parse(self.lexer.lexems)
        self.prettyPrinter.visit(self.parser.ast)
        self.assertEqual(pretty_source, self.prettyPrinter.clean_source)

    def testVisitWhileStatement(self):
        source = 'int main() {int a, b;while (a == b) {c = d;} d = e;}'
        f = open('test_resources/prettyWhileStatement.minic', 'r')
        pretty_source = f.read()
        f.close()

        self.lexer.tokenize(source)
        self.parser.parse(self.lexer.lexems)
        self.prettyPrinter.visit(self.parser.ast)
        self.assertEqual(pretty_source, self.prettyPrinter.clean_source)

    def testVisitPrettyPrint(self):
        f = open('test_resources/prettyWhileStatement.minic', 'r')
        pretty_source = f.read()
        f.close()

        self.lexer.tokenize(pretty_source)
        self.parser.parse(self.lexer.lexems)
        self.prettyPrinter.visit(self.parser.ast)
        self.assertEqual(pretty_source, self.prettyPrinter.clean_source)

    def testPrettyPrintExamples(self):
        f = open('test_resources/fibo.minic', 'r')
        pretty_source = f.read()
        f.close()

        self.lexer.tokenize(pretty_source)
        self.parser.parse(self.lexer.lexems)
        self.prettyPrinter.visit(self.parser.ast)
        self.assertEqual(pretty_source, self.prettyPrinter.clean_source)


if __name__ == '__main__':
    unittest.main()
