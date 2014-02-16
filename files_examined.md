## Files and directories examined

[edited 20140216]

1. `Grammar/Grammar`: EBNF grammar file
1. `Doc/`: Various documentation files. Directories `includes/` and `tools/` contain some `.py` files:

  2. `Doc/tools/roman.py`: Convert to and from Roman numerals.
  2. `Doc/tools/rstlint.py`: Linter for `.rst` and `.py` files.
  2. `Doc/tools/sphinx-build.py`: "Sphinx - Python documentation toolchain" (for use with Python 2.4-2.7).

1. `Doc/bugs.rst`: reST file for bug-list
1. `Include/eval.h`: header file for `eval()`
1. `Lib/difflib.py`: Python source-code for module `difflib`
1. `Modules/`: CPython modules in C-code; no `.py` files found.
1. `Objects/`: basic types in C-code; contains one Python file: `typeslots.py`. Clarifies type of various objects by renaming.
1. `Parser/`: parser in C-code; contains `ASDL` file and two Python files, such as `asdl.py`, for implementing `ASDL`.
1. `Python/`: interpreter in C-code; contains one Python file: `makeopcodetargets.py`:

   > Generate C code for the jump table of the threaded code interpreter
   > (for compilers supporting computed gotos or "labels-as-values", such as gcc).

[end]
