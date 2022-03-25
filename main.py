"""
@author Corentin Goetghebeur (github.com/CorentinGoet).
"""

from lexer import Lexer


if __name__ == '__main__':
    source_code = open('example.minic', 'r').read()
    lexer = Lexer()
    lexer.tokenize(source_code)
    print(lexer)
