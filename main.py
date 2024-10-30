###############################################################################
# main.py
#
# Top-level script for the project as a whole.
###############################################################################

# import argparse for command-line argument parsing
import argparse

# Import the lexer
import P01_LexicalAnalyzer.states as states
import P01_LexicalAnalyzer.lexer as lexer

# Import the parser
import P02_Parser.parser as parser

# Function to execute the lexer & parser
def execute(inputString):
    try:
        # Token stream
        print("Token stream:")
        print("-------------")
        tokenStream = lexer.lexer(inputString)

        # Parse the token stream
        print("\nAbstract Syntax Tree:")
        print("---------------------")
        myParser = parser.Parser()
        myParser.parse(tokenStream)
        myParser.print_ast()
    except Exception as e:
        print(f"- FATAL: {e}")

# Top-level function for the project
def main():
    # Command line parsing generated via Copilot
    #
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Process a file containing token stream.")
    parser.add_argument("filename", help="The name of the file to read.")

    # Parse the command-line arguments
    args = parser.parse_args()

    try:
        # Open and read the file
        with open(args.filename, 'r') as file:
            content = file.read()
            execute(content)
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
