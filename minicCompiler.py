#!/usr/bin/env python3
"""
@author Corentin Goetghebeur (github.com/CorentinGoet).
"""
from lexer_pkg.lexer import Lexer
from parser_pkg.parser import Parser
from CLI.CLIinterface import CLI
import sys
from CLI.actions import Actions
from pretty_printer_pkg.pretty_printer import PrettyPrinter


def main():
    """
    Main function.
    """

    cli = CLI()
    action, file = cli.process_args(sys.argv)
    src = open(file, "r").read()
    lexer = Lexer()
    parser = Parser()

    # Lexing
    try:
        lexer.tokenize(src)
    except Exception as e:
        print(f"Error during lexing: {e}")
        sys.exit(1)

    # Parsing
    try:
        parser.parse(lexer.lexems)
    except Exception as e:
        print(f"Error during parsing: {e}")
        sys.exit(1)

    # Action
    try:
        if action == Actions.PRETTY_PRINT:
            visitor = PrettyPrinter()

        elif action == Actions.COMPILE:
            print("not implemented yet")
    except Exception as e:
        print(f"Error during instantiation of the visitor: {e}")
        sys.exit(1)

    # Visitor

    try:
        visitor.visit(parser.ast)
    except Exception as e:
        print(f"Error during visitor: {e}")
        print(parser.ast)


if __name__ == '__main__':
    main()