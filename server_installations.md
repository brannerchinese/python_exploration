## Server installations

[edited 20140216]

1. `sudo apt-get install vim`
1. `sudo apt-get install lynx-cur`
1. `sudo apt-get install python-virtualenv`
1. `sudo apt-get install gdb`

   Many dependencies.

1. `virtualenv v_env3 --python=python3.3`
1. `sudo apt-get build-dep python3.3`

   Many dependencies.

1. `source v_env3/bin/activate`
1. `pip install ipython`
1. `pip freeze > requirements.txt`
1. Download and extract source-code:

        wget 'http://python.org/ftp/python/3.3.4/Python-3.3.4.tar.xz'
        tar xJvf Python-3.3.4.tar.xz

1. Configure (without the `CFLAGS="-g4"` suggested by Vivek)  and make:

        cd Python-3.3.4
        CFLAGS="-g3 -ggdb -gdwarf-4" ./configure --with-pydebug --prefix=$PWD-build
        make -j9
        make install

   See the `gcc` man page for information about the flags, starting under `-glevel`. The flag `-g3` means level 3 of `-glevel`: 
   
   > Level 3 includes extra information, such as all the macro definitions present in the program. Some debuggers support macro expansion when you use `-g3`.

1. Run using:

        $PWD-build/bin/python3


[end]