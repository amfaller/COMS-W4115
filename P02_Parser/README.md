# Programming Assignment 2
Author: Tony Faller (UNI: af3370)

This directory contains a parser that accepts the output from the lexer implemented in Programming Assignment 1 and outputs an abstract syntax tree (AST).

## Tokens
The tokens output by the lexer are as follows:
| Token Type | Regular Expression        | Notes                                                              |
|------------|---------------------------|--------------------------------------------------------------------|
| DATATYPE   | [!, @, #, $]              |                                                                    |
| ID         | [a-z A-Z]+ '.' [a-z A-Z]+ | The '.' represents the "period" or "dot" character, not a wildcard |
| OPERATOR   | [=]                       |                                                                    |
| INT        | [0-9]+                    |                                                                    |
| FLOAT      | [0-9]+ '.' [0-9]+         | The '.' represents the "period" or "dot" character, not a wildcard |
| TRUE       | [true]                    |                                                                    |
| FALSE      | [false]                   |                                                                    |
| STRING     | " [a-z]* "                | Each " represents a "double quote" charaacter                      |
| COMMENT    | { [a-z A-Z 0-9 ' ']* }    | The ' ' represents whitespace                                      |
| NEWLINE    | \n                        |                                                                    |

## Context-Free Grammar
The context-free grammar (CFG) of this parser is as follows:

```
LINE --> INT_LINE | FLOAT_LINE | BOOL_LINE | STRING_LINE

COMMON --> ID COMMENT OPERATOR

DATATYPE_INT --> '!'
INT_LINE --> DATATYPE_INT COMMON INT NEWLINE

DATATYPE_FLOAT --> '@'
FLOAT_LINE --> DATATYPE_FLOAT COMMON FLOAT NEWLINE

DATATYPE_BOOL --> '#'
BOOL_LINE --> DATATYPE_BOOL COMMON (TRUE|FALSE) NEWLINE

DATATYPE_STRING --> '$'
STRING_LINE --> DATATYPE_STRING COMMON STRING NEWLINE
```

Where `ID`, `COMMENT`, `OPERATOR`, `NEWLINE`, `INT`, `FLOAT`, `TRUE`, `FALSE`, and `STRING` are terminals defined as tokens above.

----
