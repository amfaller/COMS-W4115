# Programming Assignment 1
Author: Tony Faller (UNI: af3370)

This directory contains a scanner that processes an input source code written in the programming language that I designed. 

## Lexical Grammar
The alphabet of this language consists of the following set: 
```
[A-Z, a-z, 0-9, !, @, #, $, =, {, }, ' ', \n, ", .]
```
Note that in this context, `' '` represents whitespace, `\n` represents the newline character, `"` represents double quote, and `.` represents the character ".".

Input strings are parsed into the following token types:

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

## Dependencies
1. `python3 -m pip install pandas`

----
