#pydice

##Installation

`pip install pydice`

##Usage

###As a CLI

To run the pydice library as an interactive CLI you run the application
without arguments:

`pydice`

###From the Command Line

To run the pydice library from the command line you run the application with
arguments that will be parsed:

`pydice 1d6 + 10`

###As a library

To use pydice as a library you need to import it and then handle the output:

```
import pydice

result, rolls = pydice.roll('1d6 + 10')
```

`pydice.roll` will raise `CaughtRollParsingError` if the parsing fails.
