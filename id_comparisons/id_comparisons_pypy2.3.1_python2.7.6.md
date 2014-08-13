~~~
Python 2.7.6 (32f35069a16d, Jun 06 2014, 20:12:47)
[PyPy 2.3.1 with GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>> [1, 2, 3] == [1, 2, 3][:] 
True
>>>> id([1, 2, 3]) == id([1, 2, 3][:])
False
>>>> id([1, 2, 3][:]) == id([1, 2, 3][:])
False
>>>> x = [1, 2, 3]
>>>> x[:]
[1, 2, 3]
>>>> x == x[:]
True
>>>> id(x) == id(x[:])
False
>>>> id(x[:]) == id(x[:])
False
>>>> id(x) == id([1, 2, 3])
False
>>>> id(x[:]) == id([1, 2, 3])
False
>>>> y = x[:]
>>>> id(x) == id(y)
False
>>>> id(x[:]) == id(y[:])
False
>>>> id(y) == id([1, 2, 3])
False
>>>> # Tuples
>>>> (1, 2, 3) == (1, 2, 3)[:]
True
>>>> id((1, 2, 3)) == id((1, 2, 3)[:])
False
>>>> id((1, 2, 3)[:]) == id((1, 2, 3)[:])
False
>>>> x = (1, 2, 3)
>>>> x[:]
(1, 2, 3)
>>>> x == x[:]
True
>>>> id(x) == id(x[:])
False
>>>> id(x[:]) == id(x[:])
False
>>>> id(x) == id((1, 2, 3))
False
>>>> id(x[:]) == id((1, 2, 3))
False
>>>> y = x[:]
>>>> id(x) == id(y)
False
>>>> id(x[:]) == id(y[:])
False
>>>> id(y) == id((1, 2, 3))
False
>>>> # Strings
>>>> '123' == '123'[:]
True
>>>> id('123') == id('123'[:])
True
>>>> id('123'[:]) == id('123'[:])
True
>>>> x = '123'
>>>> x[:]
'123'
>>>> x == x[:]
True
>>>> id(x) == id(x[:])
True
>>>> id(x) == id('123')
False
>>>> id(x[:]) == id(x[:])
True
>>>> id(x[:]) == id('123')
False
>>>> y = x[:]
>>>> id(x) == id(y)
True
>>>> id(y) == id('123')
False
>>>> # array.array
>>>> import array
>>>> array.array('i', [1, 2, 3]) == array.array('i', [1, 2, 3])[:]
True
>>>> id(array.array('i', [1, 2, 3])) == id(array.array('i', [1, 2, 3])[:])
False
>>>> id(array.array('i', [1, 2, 3])[:]) == id(array.array('i', [1, 2, 3])[:])
False
>>>> x = array.array('i', [1, 2, 3])
>>>> x[:]
array('i', [1, 2, 3])
>>>> x == x[:]
True
>>>> id(x) == id(x[:])
False
>>>> id(x[:]) == id(x[:])
False
>>>> id(x) == id(array.array('i', [1, 2, 3]))
False
>>>> id(x[:]) == id(array.array('i', [1, 2, 3]))
False
>>>> y = x[:]
>>>> id(x) == id(y)
False
>>>> id(x[:]) == id(y[:])
False
>>>> id(y) == id(array.array('i', [1, 2, 3]))
False
>>>> # bytes objects
>>>> bytes(123) == bytes(123)[:]
True
>>>> id(bytes(123)) == id(bytes(123)[:])
False
>>>> id(bytes(123)[:]) == id(bytes(123)[:])
False
>>>> x = bytes(123)
>>>> x[:]
'123'
>>>> x == x[:]
True
>>>> id(x) == id(x[:])
True
>>>> id(x[:]) == id(x[:])
True
>>>> id(x) == id(bytes(123))
False
>>>> id(x[:]) == id(bytes(123))
False
>>>> y = x[:]
>>>> id(x) == id(y)
True
>>>> id(x[:]) == id(y[:])
True
>>>> id(y) == id(bytes(123))
False
>>>> 
~~~