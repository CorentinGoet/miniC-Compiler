"""
@author Corentin Goetghebeur (github.com/CorentinGoet)

Python CLI interface for the project.
"""
import sys
from CLI.actions import Actions


class CLI:

    def __init__(self):
        f = open("resources/title.txt", "r")
        self.title = f.read()
        f.close()

    def display_title(self):
        """
        Display the title of the program.
        :return: None
        """
        print(self.title)

    def display_usage(self):
        """
        Display the usage help
        :return: None
        """
        print("Usage:")
        print("\tminic-compiler <action> [file]")
        print("Actions:")
        print("\tcompile\t\t\tCompile a file to SIMJI assembly code. (not implemented yet)")
        print("\tpretty-print\tPretty print a mini-C program.")
        print("\ttest\t\t\tRun the tests.")
        print("\thelp\t\t\tDisplay this help.")

    def display_menu(self):
        """
        Display the menu.
        :return: None
        """
        print("MiniC-Compiler is a compiler for a simplified version of the C language called Mini-C.")
        print("To learn more about the project read the project's README file or "
              "visit the GitHub repo: github.com/CorentinGoet/miniC-Compiler.")
        print("\n")
        print("Mini-C compiler can be used to pretty-print a Mini-C program or to compile it \nto assembly code for the"
              "SIMJI Instruction Set Simulator: github.com/CorentinGoet/SIMJI.\n")

    def process_args(self, args):
        """
        Process the arguments passed to the program.
        :param args: list of arguments
        :return: action, file
        """
        if len(args) < 2:
            self.display_title()
            self.display_menu()
            self.display_usage()
            sys.exit(1)

        if len(args) == 2:
            if args[1] == "help":
                action = Actions.HELP

            elif args[1] == "test":
                action = Actions.TEST

            else:
                self.display_title()
                self.display_menu()
                self.display_usage()
                sys.exit(1)

            return action, None

        action = args[1]
        file = args[2]
        try:
            f = open(file, "r")
            f.close()
        except FileNotFoundError:
            print(f"File not found: {file}")
            sys.exit(1)

        if action == "pretty-print":
            return Actions.PRETTY_PRINT, file

        if action == "compile":
            return Actions.COMPILE, file
