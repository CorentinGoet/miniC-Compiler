"""
@author Corentin Goetghebeur (github.com/CorentinGoet).
"""

from lexer import Lexer
from parser import Parser


if __name__ == '__main__':
    source_code = open('example.minic', 'r').read()
    lexer = Lexer()
    lexer.tokenize(source_code)
    print(lexer)
    parser = Parser()
    ast = parser.parse(lexer.lexems)
    print(ast)

