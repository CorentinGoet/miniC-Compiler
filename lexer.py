"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

from lexem import Lexem, LexemTag
import re


class Lexer:
    """
    The lexer is in charge of breaking the source code into lexems.
    It matches the text from the source code with the lexem tags using regex.
    """

    regexExpressions = [
        (r'main', LexemTag.MAIN),
        (r'\(', LexemTag.L_PARENTHESIS),
        (r'\)', LexemTag.R_PARENTHESIS),
        (r'\[', LexemTag.L_BRACKET),
        (r'\]', LexemTag.R_BRACKET),
        (r'\{', LexemTag.L_BRACE),
        (r'\}', LexemTag.R_BRACE),
        (r'\+', LexemTag.ADDITION),
        (r'\-', LexemTag.SUBTRACTION),
        (r'\*', LexemTag.MULTIPLICATION),
        (r'\/', LexemTag.DIVISION),
        (r'\%', LexemTag.MODULO),
        (r'\;', LexemTag.TERMINATOR),
        (r'\=', LexemTag.ASSIGNMENT),
        (r'int |float |char |bool ', LexemTag.TYPE),
        (r'true|false', LexemTag.BOOL),
        (r'([a-zA-Z](\d|[a-zA-Z])*)', LexemTag.IDENTIFIER),
        (r'\d+', LexemTag.INTEGER),
        (r'\d+\.\d+', LexemTag.FLOAT),
        (r"\'(.)\'", LexemTag.CHAR),

        (r'[ \n\t]+', None),
    ]

    def __init__(self):
        """
        Initializes the lexer with the source code.
        """
        self.lexems = []

    def tokenize(self, source_code):
        """
        Tokenizes the source code.
        For each detected lexem, it creates a Lexem object and adds it to the list of lexems.

        :param source_code: The source code to tokenize.
        """

        # Go through each line of the source code
        for lineNumber, line in enumerate(source_code.split('\n')):
            lineNumber += 1
            position = 0

            # Go through the line
            while position < len(line):
                match = None
                for pattern, tag in self.regexExpressions:
                    regex = re.compile(pattern)
                    match = regex.match(line, position)
                    if match:
                        data = match.group(0)
                        lex = Lexem(tag, data, [lineNumber, position])
                        if lex.value is not None:
                            self.lexems.append(lex)
                        position = match.end()
                        break
            if not match:
                errMsg = "Syntax error at line {} position {}.\n".format(lineNumber, position)
                errMsg += "Unrecognized token: \n {}".format(line)
                errMsg += "\n" + " " * (position + 1) + "^"
                raise Exception(errMsg)

    def __str__(self):
        """
        Returns a string representation of the lexems.
        """
        return '\n'.join([str(lexem) for lexem in self.lexems])
