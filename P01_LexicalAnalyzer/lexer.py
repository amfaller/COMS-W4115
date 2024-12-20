###############################################################################
# lexer.py
#
# Top-level script for the lexical analyzer.
###############################################################################

from .states import State 
from .states import Transitions

# Global Transitions object
transitions = Transitions()

# Function to print output based on the state
def print_output(state, token):
    stateAsString = transitions.state_to_string(state)
    print(f"<{stateAsString}, {token}>")

# Function that takes an input string and parses it per the transitions
def lexer(inputString):
    # Initialize the state to INITIAL
    state = State.INITIAL
    currentToken = ""

    # Output list
    output = []

    # Iterate through the input string
    strIdx = 0
    while strIdx < len(inputString):
        char = inputString[strIdx]

        # Special case: If char is newline, want to pass "\\n" to the transition function
        if char == "\n":
            char = "\\n"

        # Append the character to the current token
        currentToken += char

        # Transition to the next state
        nextState = transitions.transition(state, char)

        # MAXIMAL MUNCH:
        # If the next state is an error, check if the current state is accepting.
        if nextState == State.ERROR:
            if transitions.is_accepting(state):
                # Check if the last character is "\n", which is added with a newline for processing.
                # Remove it now.
                if currentToken[-2:] == "\\n":
                    currentToken = currentToken[:-1]

                # If we're in an accepting state, it means that the current token is complete.
                # Need to backtrack by one character and print the token.
                currentToken = currentToken[:-1]
                print_output(state, currentToken)

                # Push to output
                output.append((transitions.state_to_string(state), currentToken))

                # Reset the index to the removed character
                strIdx -= 1

                # Reset state and token
                state = State.INITIAL
                currentToken = ""
                
            else:
                raise Exception(f"Error: Invalid token encountered: {currentToken}")

            # Reset & continue
            state = State.INITIAL
            currentToken = ""
        else:
            # If the next state is not an error, update the state
            state = nextState

        # Increment the string index
        strIdx += 1

    # Print the final token if it's in an accepting state
    if transitions.is_accepting(state):
        print_output(state, currentToken)

        # Push to output
        output.append((transitions.state_to_string(state), currentToken))

    else:
        raise Exception(f"Error: Invalid token encountered: {currentToken}")

    return output

# Top-level method called when the script is run
def main():
    print("This should not be called!")

if __name__ == "__main__":
    main()