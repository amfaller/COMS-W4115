# Programming Assignment 1
Author: Tony Faller (UNI: af3370)

This directory contains a scanner that processes an input source code written in the programming language that I designed. 

## Lexical Grammar
The alphabet of this language consists of the following set: 
```
[A-Z, a-z, 0-9, !, @, #, $, =, {, }, ' ', \n, ", .]
```
Note that in this context, `' '` represents whitespace, `\n` represents the newline character, `"` represents double quote, and `.` represents the character ".".

Input strings are parsed into the following tokens:

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



## Sample Input/Output
The following is expected when the Docker container is executed:

```
>> Testing string: !MyNvp.enableSomeFunctionality{this is a boolean}=true
<DATATYPE, !>
<ID, MyNvp.enableSomeFunctionality>
<COMMENT, {this is a boolean}>
<EQUAL, =>
<TRUE, true>

>> Testing string: @MyNvp.someIntegerValue{}=5
<DATATYPE, @>
<ID, MyNvp.someIntegerValue>
<COMMENT, {}>
<EQUAL, =>
<INT, 5>

>> Testing string: @MyNvp.someOtherIntegerValue{Comment}=24
<DATATYPE, @>
<ID, MyNvp.someOtherIntegerValue>
<COMMENT, {Comment}>
<EQUAL, =>
<INT, 24>

>> Testing string: #MyNvp.ThisIsAFloat{Comment}=3.14
<DATATYPE, #>
<ID, MyNvp.ThisIsAFloat>
<COMMENT, {Comment}>
<EQUAL, =>
<FLOAT, 3.14>

>> Testing string: $MyNvp.StringTest{}="This is a string"
<DATATYPE, $>
<ID, MyNvp.StringTest>
<COMMENT, {}>
<EQUAL, =>
<STRING, "This is a string">

>> Testing string: This should produce errors
<ERROR, This >
<ERROR, should >
<ERROR, produce >
<ERROR, errors>

>> Testing string: "This should NOT produce any errors"
<STRING, "This should NOT produce any errors">
```

## State Machine
This scanner is implemented as a state machine with 26 states. A hand-drawn diagram of this state machine is available in the [Programming Assignment 1 Scratch.pdf](./Programming%20Assignment%201%20Scratch.pdf) file in this directory.

A table representation of this state machine is available in the [StateTable.csv](./StateTable.csv) file in this directory. The leftmost column represents states, and the headers represent the input alphabet.

----
