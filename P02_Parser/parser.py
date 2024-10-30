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
class Parser:
    def __init__(self):
        pass

    # The first method in the recursive descent parser
    def parse_root(self):
        # Get the number of tokens
        numTokens = len(self.tokens)

        

        # Position in the grammar:
        #  0 - datatype
        #  1 - ID
        #  2 - comment
        #  3 - operator
        #  4 - value
        #  5 - newline
        grammarPosition = 0

        # Datatypes: 
        #  0 - int
        #  1 - float
        #  2 - bool
        #  3 - string
        dataType = -1

        # Iterate through the tokens
        while self.idx < numTokens:
            # Get the current token
            token = self.tokens[self.idx]

            if grammarPosition == 0:
                # Since we're parsing such a rigid grammar, we can easily
                # determine the position of a given node in the AST based
                # on the position in the grammar.
                lineNode = Node("LINE", "")
                dataTypeNode = Node("DATATYPE", "")
                commonNode = Node("COMMON", "")
                commonNode_ID = Node("ID", "")
                commonNode_COMMENT = Node("COMMENT", "")
                commonNode_OPERATOR = Node("OPERATOR", "")
                valueNode = Node("VALUE", "")
                newlineNode = Node("NEWLINE", "")

                self.root.add_child(lineNode)

                lineNode.add_child(dataTypeNode)
                lineNode.add_child(commonNode)
                lineNode.add_child(valueNode)
                lineNode.add_child(newlineNode)

                commonNode.add_child(commonNode_ID)
                commonNode.add_child(commonNode_COMMENT)
                commonNode.add_child(commonNode_OPERATOR)

                # Always expect the first token to be a datatype
                if isDatatype(token[0]):
                    if isDatatypeInt(token[1]):
                        lineNode.type = "INT_LINE"
                        dataTypeNode.type = "DATATYPE_INT"
                        dataTypeNode.value = token[1]
                        self.idx += 1
                        dataType = 0
                    elif isDatatypeFloat(token[1]):
                        lineNode.type = "FLOAT_LINE"
                        dataTypeNode.type = "DATATYPE_FLOAT"
                        dataTypeNode.value = token[1]
                        self.idx += 1
                        dataType = 1
                    elif isDatatypeBool(token[1]):
                        lineNode.type = "BOOL_LINE"
                        dataTypeNode.type = "DATATYPE_BOOL"
                        dataTypeNode.value = token[1]
                        self.idx += 1
                        dataType = 2
                    elif isDatatypeString(token[1]):
                        lineNode.type = "STRING_LINE"
                        dataTypeNode.type = "DATATYPE_STRING"
                        dataTypeNode.value = token[1]
                        self.idx += 1
                        dataType = 3
                    else:
                        print(f"Error: Unexpected token {token}")
                        return
                else:
                    print(f"Error: Unexpected token {token}")
                    return
                
            # Expect an ID token next
            if grammarPosition == 1:
                if not isID(self.tokens[self.idx][0]):
                    print(f"Error: Expected ID token, got {self.tokens[self.idx]}")
                    return
                else:
                    commonNode_ID.value = self.tokens[self.idx][1]
                    self.idx += 1

            # Now a comment
            if grammarPosition == 2:
                if not isComment(self.tokens[self.idx][0]):
                    print(f"Error: Expected COMMENT token, got {self.tokens[self.idx]}")
                    return
                else:
                    commonNode_COMMENT.value = self.tokens[self.idx][1]
                    self.idx += 1

            # Expect an operator
            if grammarPosition == 3:
                if not isOperator(self.tokens[self.idx][0]):
                    print(f"Error: Expected EQUAL token, got {self.tokens[self.idx]}")
                    return
                else:
                    commonNode_OPERATOR.value = self.tokens[self.idx][1]
                    self.idx += 1

            # Expect a value depending on the datatype
            if grammarPosition == 4:
                if dataType == 0:
                    if not isInt(self.tokens[self.idx][0]):
                        print(f"Error: Expected INT token, got {self.tokens[self.idx]}")
                        return
                    else:
                        valueNode.type = "INT"
                        valueNode.value = self.tokens[self.idx][1]
                        self.idx += 1
                elif dataType == 1:
                    if not isFloat(self.tokens[self.idx][0]):
                        print(f"Error: Expected FLOAT token, got {self.tokens[self.idx]}")
                        return
                    else:
                        valueNode.type = "FLOAT"
                        valueNode.value = self.tokens[self.idx][1]
                        self.idx += 1
                elif dataType == 2:
                    if not isBool(self.tokens[self.idx][0]):
                        print(f"Error: Expected BOOL token, got {self.tokens[self.idx]}")
                        return
                    else:
                        valueNode.type = "BOOL"
                        valueNode.value = self.tokens[self.idx][1]
                        self.idx += 1
                elif dataType == 3:
                    if not isString(self.tokens[self.idx][0]):
                        print(f"Error: Expected STRING token, got {self.tokens[self.idx]}")
                        return
                    else:
                        valueNode.type = "STRING"
                        valueNode.value = self.tokens[self.idx][1]
                        self.idx += 1

            # Expect a newline
            if grammarPosition == 5:
                if self.tokens[self.idx][0] and not isNewline(self.tokens[self.idx][0]):
                    print(f"Error: Expected NEWLINE token, got {self.tokens[self.idx]}")
                    return
                else:
                    newlineNode.value = self.tokens[self.idx][1]
                    self.idx += 1

            # Move to the next position in the grammar
            grammarPosition = (grammarPosition + 1) % 6

        # When we're done iterating, we should be at grammar position 0
        if grammarPosition != 0:
            print("Error: Unexpected end of input")
            return


    def parse(self, tokens):
        # Initialize the index to 0
        self.idx = 0
        self.tokens = tokens

        # Initialize the root node
        self.root = Node("ROOT", "")

        # Start parsing
        self.parse_root()

        # Print the AST
        print_ast(self.root)

        return self.root


if __name__ == "__main__":
    print("This should not be called!")

