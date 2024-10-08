###############################################################################
# states.py
#
# Define the states of the lexical analyzer finite state machine.
# These states are based off of the FSM diagram in the project.
###############################################################################

from enum import Enum
import pandas as pd

class State(Enum):
    # Starting state
    INITIAL = 0

    # Datatype
    DATATYPE = 1    # Accepting state

    # ID
    ID_BEGIN = 2
    ID_PERIOD = 3
    ID_END = 4      # Accepting state

    # "true"
    TRUE_T = 5
    TRUE_R = 6
    TRUE_U = 7
    TRUE_E = 8      # Accepting state

    # "false"
    FALSE_F = 9
    FALSE_A = 10
    FALSE_L = 11
    FALSE_S = 12
    FALSE_E = 13    # Accepting state

    # "="
    EQUAL = 14      # Accepting state

    # Number types
    INT = 15       # Accepting state
    FLOAT_PERIOD = 16
    FLOAT = 17     # Accepting state

    # String
    STRING_QUOTE_BEGIN = 18
    STRING_INNER = 19
    STRING_QUOTE_END = 20   # Accepting state

    # Comments
    COMMENT_CURLY_BRACKET_BEGIN = 21
    COMMENT_INNER = 22
    COMMENT_CURLY_BRACKET_END = 23  # Accepting state

    # Newline
    NEWLINE = 24    # Accepting state

    # Error state
    ERROR = 25

    # Table representing state transitions
    transitionTable = []
    
    # Function to load the CSV table representing state transitions
    # This table has states in the leftmost column and input characters as the headers
    @staticmethod
    def load_table():
        # Load the CSV table
        table = pd.read_csv('transition_table.csv')

    # Function to get the next state based on the current state and input character
    @staticmethod
    def transition(current_state, input_char):
        # Get the next state from the transition table
        next_state = State.transitionTable.loc[current_state.name, input_char]

        # If the next state is NaN, return the ERROR state
        if pd.isna(next_state):
            return State.ERROR
        else:
            return State[next_state]

    # Initialization
    def __init__(self):
        self.transitionTable = State.load_table()

    