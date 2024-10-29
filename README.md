# COMS-W4115
Repository for the semester-long COMS W4115 project in Fall 2024

## Programming Assignment 1
### Technical Write-Up
Please see [P01_LexicalAnalyzer/README.md](./P01_LexicalAnalyzer/README.md).

### Installation
For convenience, a Dockerfile is included in this directory. To execute the basic lexer with sample inputs, perform the following:
1. Install Docker
2. Execute `docker build -t nvp-img .` to build the docker image
3. Execute `docker run nvp-img` to run the container.

Alternatively, if the target environment has Python3.4 or later installed with the `pandas` package, one can simply execute:
```
python3 lexer.py
```
for the same effect. To install `pandas`, run:
```
python3 -m pip install pandas
```

----
