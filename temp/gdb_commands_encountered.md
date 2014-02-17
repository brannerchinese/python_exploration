## gdb commands encountered

[edited 20140216]

### To run

    gdb --args .../bin/python3

An alias to this, `py`, has been placed in `.bash-profile`.

### Commands

1. `tbreak`: set temporary breakpoint (deleted once hit).
1. `break`: set permanent breakpoint.
1. `continue`: continue after signal or breakpoint.
1. `list`: list specified function or line.
1. `info macro X`: get information about C macro X
1. `info function X`: get information about C function X
1. `backtrace`: print backtrace of all stack frames
1. `step`: step program until it reaches a different source line.
1. `next`: like `step`, but steps over subroutines rather than entering them.
1. `finish`: execute until selected stack frame returns.

[end]