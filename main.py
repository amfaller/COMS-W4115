###############################################################################
# main.py
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
    notUsed = lexer.lexer(testString)
    print()

    testString = "@MyNvp.someIntegerValue{}=5"
    print(f">> Testing string: {testString}")
    notUsed = lexer.lexer(testString)
    print()

    testString = "@MyNvp.someOtherIntegerValue{Comment}=24"
    print(f">> Testing string: {testString}")
    notUsed = lexer.lexer(testString)
    print()

    testString = "#MyNvp.ThisIsAFloat{Comment}=3.14"
    print(f">> Testing string: {testString}")
    notUsed = lexer.lexer(testString)
    print()

    testString = "$MyNvp.StringTest{}=\"This is a string\""
    print(f">> Testing string: {testString}")
    notUsed = lexer.lexer(testString)
    print()

    testString = "This should produce errors"
    print(f">> Testing string: {testString}")
    notUsed = lexer.lexer(testString)
    print()

    testString = "\"This should NOT produce any errors\""
    print(f">> Testing string: {testString}")
    notUsed = lexer.lexer(testString)
    print()

if __name__ == "__main__":
    main()
