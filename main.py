###############################################################################
# main.py
#
# Top-level script for the project as a whole.
###############################################################################

# Import the lexer
import P01_LexicalAnalyzer.states as states
import P01_LexicalAnalyzer.lexer as lexer

# Import the parser
import P02_Parser.parser as parser

# Top-level function for the project
def main():
    testString = "#MyNvp.enableSomeFunctionality{this is a boolean}=true\n"
    print(f">> Testing string: {testString}")

    print("Token stream:")
    print("-------------")
    tokenStream = lexer.lexer(testString)

    print()

    print("AST: ")
    print("-------------")
    myParser = parser.Parser()
    myParser.parse(tokenStream)

if __name__ == "__main__":
    main()
