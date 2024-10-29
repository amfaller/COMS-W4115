###############################################################################
# helpers.py
#
# Helper methods for the parser.
###############################################################################

###################
# Common
###################
def isID(s):
    return s == "ID"

def isComment(s):
    return s == "COMMENT"

def isOperator(s):
    return s == "EQUAL"

def isNewline(s):
    return s == "NEWLINE"

###################
# Integers
###################
def isDatatypeInt(s):
    return s == "!"

def isInt(s):
    return s == "INT"

###################
# Floats
###################
def isDatatypeFloat(s):
    return s == "@"

def isFloat(s):
    return s == "FLOAT"

###################
# Booleans
###################
def isDatatypeBool(s):
    return s == "#"

def isBool(s):
    return s == "TRUE" or s == "FALSE"

###################
# Strings
###################
def isDatatypeString(s):
    return s == "$"

def isString(s):
    return s == "STRING"

