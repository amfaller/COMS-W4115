# COMS-W4115
Repository for the semester-long COMS W4115 project in Fall 2024.

Author: Tony Faller (af3370)

## Programming Assignment 1
### Technical Write-Up
Please see [P01_LexicalAnalyzer/README.md](./P01_LexicalAnalyzer/README.md).

## Programming Assignment 2
### Technical Write-Up
Please see [P02_Parser/README.md](./P02_Parser/README.md).

### Demo Video
A demo video for Programming Assignment 2 is available [here](https://youtu.be/WvFzBS5Y88I).

## Programming Assignment 3
### Technical Write-Up
Please see [P03_CodeGen/README.md](./P03_CodeGen/README.md).

### Demo Video
A demo video for Programming Assignment 3 is available [here](TODO). (TODO)

## Installation
For convenience, a Dockerfile is included in this directory. To execute the basic lexer with sample inputs, perform the following:
1. Install Docker
2. Execute `docker build -t nvp-img .` to build the docker image
3. Execute `docker run nvp-img` to run the container.

Alternatively, if the target environment has Python3.4 or later installed with the `pandas` package, one can simply execute:
```
python3 main.py test.nvp
```

## Expected Output
As of Programming Assignment 2, this is the expected output when the Docker image is executed:
```
Token stream:
-------------
<DATATYPE, !>
<ID, test.ThisIsAnInteger>
<COMMENT, {}>
<EQUAL, =>
<INT, 24>
<NEWLINE, \n>
<DATATYPE, @>
<ID, second.Identifier>
<COMMENT, {float}>
<EQUAL, =>
<FLOAT, 2.2>
<NEWLINE, \n>
<DATATYPE, #>
<ID, MyNvp.enableSomeFunctionality>
<COMMENT, {this is a boolean}>
<EQUAL, =>
<TRUE, true>
<NEWLINE, \n>
<DATATYPE, $>
<ID, Hey.ThisOneIsAString>
<COMMENT, {comment}>
<EQUAL, =>
<STRING, "Hello world">
<NEWLINE, \n>
<DATATYPE, !>
<ID, OneMOre.mAkEs>
<COMMENT, {Five}>
<EQUAL, =>
<INT, 5>
<NEWLINE, \n>

Abstract Syntax Tree:
---------------------
ROOT: 
  INT_LINE: 
    DATATYPE_INT: !
    COMMON: 
      ID: test.ThisIsAnInteger
      COMMENT: {}
      OPERATOR: =
    INT: 24
    NEWLINE: \n
  FLOAT_LINE: 
    DATATYPE_FLOAT: @
    COMMON: 
      ID: second.Identifier
      COMMENT: {float}
      OPERATOR: =
    FLOAT: 2.2
    NEWLINE: \n
  BOOL_LINE: 
    DATATYPE_BOOL: #
    COMMON: 
      ID: MyNvp.enableSomeFunctionality
      COMMENT: {this is a boolean}
      OPERATOR: =
    BOOL: true
    NEWLINE: \n
  STRING_LINE: 
    DATATYPE_STRING: $
    COMMON: 
      ID: Hey.ThisOneIsAString
      COMMENT: {comment}
      OPERATOR: =
    STRING: "Hello world"
    NEWLINE: \n
  INT_LINE: 
    DATATYPE_INT: !
    COMMON: 
      ID: OneMOre.mAkEs
      COMMENT: {Five}
      OPERATOR: =
    INT: 5
    NEWLINE: \n
```

----
