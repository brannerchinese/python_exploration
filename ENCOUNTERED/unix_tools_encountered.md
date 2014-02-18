## Unix tools

[edited 20140217]

### Apt-get etc.

1. `apt-cache search <package>`: Search the package list for a regex pattern
1. `apt-cache show <package>`: Show a readable record for the package
1. `apt-get build-dep <package>`: Configure build-dependencies for source packages.

### Other programs

1. `build-essential`: Informational list of build-essential packages.
1. `ssh-agent` (execute as ``eval `ssh-agent -s` ``) and `ssh-add`
1. `xargs`: build and execute command lines from standard input

  2. `-print0`: print the full file name on the standard output,  followed by  a  null  character  (instead  of  the newline character that `-print` uses). This option corresponds  to the `-0` option of `xargs`.

[end]
