# Programming Assignment 3
Author: Tony Faller (UNI: af3370)

This directory contains a code generator which accepts the Abstract Syntax Tree (AST) generated in Programming Assignment 2 and generates lower-level code.

The original goal of this language was to implement some mechanism by which `const` C++ variables could be modified between executions without needing to recompile the C++ source code. As one can imagine, C++ projects can become quite large, and recompilation can take quite a long time.

This is accomplied by first translating the NVP syntax into an intermediate XML file, then parsing that XML file in C++. When values are modified in an NVP file, the XML file must be regenerated, but the C++ code need not be recompiled.

## Compilation Steps

A sample usage of this language from C++ is provided in [SampleClient.cpp](../SampleClient.cpp). This file only needs to be built once, with the following command:
```
g++ SampleClient.cpp tinyxml2/tinyxml2.cpp -std=c++11 -o sample
```

Each time values in test.nvp are modified, the intermediary XML file can be generated via:
```
python3 main.py test.nvp
```

And the effects of these value updates can be seen by running `./sample` _without_ rebuilding SampleClient.cpp.

## Considerations
Any time a new entry is added to an NVP file, a corresponding XML query must be added to the C++ file which pulls in this value. This will require a rebuild of the C++ source code.

----
