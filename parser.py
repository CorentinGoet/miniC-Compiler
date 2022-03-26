"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""
import sys
from lexem import LexemTag
from AST import *


class Parser:
    """
    The parser takes the lexems from the lexer and builds the AST.
    """

    def __init__(self):
        self.lexems = []

    def peek(self, n: int=1):
        """
        Returns the nth next lexem without consuming it.
        """
        if len(self.lexems) > n:
            return self.lexems[n]
        else:
            print("Error: no more lexems to peek.")
            sys.exit(1)

    def expect(self, tag: LexemTag):
        """
        pops the next lexem and tests its type.
        """
        lexem = self.peek()
        if lexem.tag == tag:
            return self.accept()
        else:
            print("Error: expected " + tag.name + " but got " + lexem.tag.name)

    def accept(self):
        """
        Accepts the next lexem and returns it.
        """
        return self.lexems.pop(0)

    def parse(self, lexems):
        """
        Parses the lexems and returns the AST.
        """
        programNode = Program()

    def parse_program(self):
        """
        Parses the program lexem.
        """
        pass

    def parse_block(self):
        """
        Parses the block lexem.
        """
        pass

    def parse_statements(self):
        """
        Parses the statements lexem.
        """
        pass

    def parse_statement(self):
        """
        Parses the statement lexem.
        """
        pass

    def parse_expression(self):
        """
        Parses the expression lexem.
        """
        pass

    def parse_assignment(self):
        """
        Parses the assignment lexem.
        """
        pass

    def parse_ifStatement(self):
        """
        Parses the ifStatement lexem.
        """
        pass

    def parse_whileStatement(self):
        """
        Parses the whileStatement lexem.
        """
        pass

    def parse_declarations(self):
        """
        Parses the declarations lexem.
        """
        pass

    def parse_declaration(self):
        """
        Parses the declaration lexem.
        """
        pass

    def parse_type(self):
        """
        Parses the type lexem.
        """
        pass

    def parse_conjunction(self):
        """
        Parses the conjunction lexem.
        """
        pass

    def parse_equality(self):
        """
        Parses the equality lexem.
        """
        pass

    def parse_equop(self):
        """
        Parses the equop lexem.
        """
        pass

    def parse_relop(self):
        """
        Parses the relop lexem.
        """
        pass

    def parse_addop(self):
        """
        Parses the addop lexem.
        """
        pass

    def parse_relation(self):
        """
        Parses the relation lexem.
        """
        pass

    def parse_term(self):
        """
        Parses the term lexem.
        """
        pass

    def parse_factor(self):
        """
        Parses the factor lexem.
        """
        pass

    def parse