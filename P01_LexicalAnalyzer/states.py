###############################################################################
# states.py
#
# Define the states of the lexical analyzer finite state machine.
# These states are based off of the FSM diagram in the project.
###############################################################################

from enum import Enum
import pandas as pd
import os

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

class Transitions:
    # Table representing state transitions
    #transitionTable = None
    
    # Initialization
    def __init__(self):
        self.transitionTable = None
    
    # Function to load the CSV table representing state transitions
    # This table has states in the leftmost column and input characters as the headers
    def load_table(self):
        # Load the CSV table
        currentDir = os.path.dirname(os.path.realpath(__file__))
        csvPath = os.path.join(currentDir, "StateTable.csv")
        self.transitionTable = pd.read_csv(csvPath)

    # Function to get the next state based on the current state and input character
    def transition(self, current_state, input_char):
        if self.transitionTable is None:
            self.load_table()

        # Get the next state from the transition table
        next_state = State.ERROR

        try:
            next_state = self.transitionTable.at[current_state.value, input_char]
        except KeyError:
            return State.ERROR

        # If the next state is NaN, return the ERROR state
        if pd.isna(next_state):
            return State.ERROR
        else:
            return State(next_state)

    # Method to check if a state is an accepting state
    def is_accepting(self, state):
        return state in [State.DATATYPE, State.ID_END, State.TRUE_E, State.FALSE_E, State.EQUAL, State.INT, State.FLOAT, State.STRING_QUOTE_END, State.COMMENT_CURLY_BRACKET_END, State.NEWLINE]

    # Method to translate a state enum to a string
    def state_to_string(self, state):
        if state == State.DATATYPE:
            return "DATATYPE"
        elif state == State.ID_END:
            return "ID"
        elif state == State.TRUE_E:
            return "TRUE"
        elif state == State.FALSE_E:
            return "FALSE"
        elif state == State.EQUAL:
            return "EQUAL"
        elif state == State.INT:
            return "INT"
        elif state == State.FLOAT:
            return "FLOAT"
        elif state == State.STRING_QUOTE_END:
            return "STRING"
        elif state == State.COMMENT_CURLY_BRACKET_END:
            return "COMMENT"
        elif state == State.NEWLINE:
            return "NEWLINE"
        else:
            return "ERROR"
    