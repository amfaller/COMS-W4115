###############################################################################
# lexer.py
#
# Top-level script for the lexical analyzer.
###############################################################################

from states import State, Transitions

# Top-level method called when the script is run
def main():
    print("Hello, world!")

    # Create a Transitions object
    transitions = Transitions()

    # Test: Transition from INITIAL with character "!"
    outState = transitions.transition(State.INITIAL, "!")
    print(outState) # Should print State.DATATYPE

if __name__ == "__main__":
    main()