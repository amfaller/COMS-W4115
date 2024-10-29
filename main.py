###############################################################################
# lexer.py
#
# Top-level script for the project as a whole.
###############################################################################

# Import the lexer
import P01_LexicalAnalyzer.states as states
import P01_LexicalAnalyzer.lexer as lexer

# Top-level function for the project
def main():
    testString = "!MyNvp.enableSomeFunctionality{this is a boolean}=true"
    print(f">> Testing string: {testString}")
    lexer.lexer(testString)
    print()

if __name__ == "__main__":
    main()
