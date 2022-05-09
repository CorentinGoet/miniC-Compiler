#!/usr/bin/env python3
"""
@author Corentin Goetghebeur (github.com/CorentinGoet).
"""

from lexer import Lexer
from parser import Parser
from CLIinterface import CLI
import sys
import time


def main():
    """
    Main function.
    """

    cli = CLI()
    file, action = cli.process_args(sys.argv)



if __name__ == '__main__':
    main()

