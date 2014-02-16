## Server installations

[edited 20140216]

1. `sudo apt-get install vim`
1. `sudo apt-get install lynx-cur`
1. `sudo apt-get install python-virtualenv`

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
        CFLAGS="-ggdb -gdwarf-4" ./configure --with-pydebug --prefix=$PWD-build
        make -j9
        make install

1. Run using:

        $PWD-build/bin/python3


[end]