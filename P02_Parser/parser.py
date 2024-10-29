###############################################################################
# parser.py
#
# The parser itself.
###############################################################################

from .helpers import *

# Define a class to serve as the node of the AST
class Node:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Define a class to serve as the parser
class Parser(self):
    def __init__(self):
        pass

    # The first method in the recursive descent parser
    def parse_root(self):
        # Get the number of tokens
        numTokens = len(self.tokens)

        # Iterate through the tokens
        while self.idx < numTokens:
            # Get the current token
            token = self.tokens[self.idx]

            # Always expect the first token to be a datatype
            if isDatatypeInt(token):
                self.root.add_child(Node(token[0], token[1]))
                self.idx += 1
                self.parse_int_line()
            elif isDatatypeFloat(token):
                self.root.add_child(Node(token[0], token[1]))
                self.idx += 1
                self.parse_float_line()
            elif isDatatypeBool(token):
                self.root.add_child(Node(token[0], token[1]))
                self.idx += 1
                self.parse_bool_line()
            elif isDatatypeString(token):
                self.root.add_child(Node(token[0], token[1]))
                self.idx += 1
                self.parse_string_line()
            else:
                print(f"Error: Unexpected token {token}")
                return

    def parse(self, tokens):
        # Initialize the index to 0
        self.idx = 0
        self.tokens = tokens

        # Initialize the root node
        self.root = Node("ROOT", "")

        # Start parsing
        self.parse_root(tokens, self.root)

        # Print the AST
        print_ast(self.root)

        return self.root


if __name__ == "__main__":
    print("This should not be called!")

