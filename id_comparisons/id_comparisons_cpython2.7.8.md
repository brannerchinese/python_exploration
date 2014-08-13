Python 2.7.8 (default, Jul  2 2014, 10:14:46) 
[GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.40)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> [1, 2, 3] == [1, 2, 3][:] 
True
>>> id([1, 2, 3]) == id([1, 2, 3][:])
False
>>> id([1, 2, 3][:]) == id([1, 2, 3][:])
False
>>> x = [1, 2, 3]
>>> x[:]
[1, 2, 3]
>>> x == x[:]
True
>>> id(x) == id(x[:])
False
>>> id(x[:]) == id(x[:])
True
>>> id(x) == id([1, 2, 3])
False
>>> id(x[:]) == id([1, 2, 3])
True
>>> y = x[:]
>>> id(x) == id(y)
False
>>> id(x[:]) == id(y[:])
True
>>> id(y) == id([1, 2, 3])
False
>>> # Tuples
>>> (1, 2, 3) == (1, 2, 3)[:]
True
>>> id((1, 2, 3)) == id((1, 2, 3)[:])
False
>>> id((1, 2, 3)[:]) == id((1, 2, 3)[:])
False
>>> x = (1, 2, 3)
>>> x[:]
(1, 2, 3)
>>> x == x[:]
True
>>> id(x) == id(x[:])
True
>>> id(x[:]) == id(x[:])
True
>>> id(x) == id((1, 2, 3))
False
>>> id(x[:]) == id((1, 2, 3))
False
>>> y = x[:]
>>> id(x) == id(y)
True
>>> id(x[:]) == id(y[:])
True
>>> id(y) == id((1, 2, 3))
False
>>> # Strings
>>> '123' == '123'[:]
True
>>> id('123') == id('123'[:])
True
>>> id('123'[:]) == id('123'[:])
True
>>> x = '123'
>>> x[:]
'123'
>>> x == x[:]
True
>>> id(x) == id(x[:])
True
>>> id(x) == id('123')
True
>>> id(x[:]) == id(x[:])
True
>>> id(x[:]) == id('123')
True
>>> y = x[:]
>>> id(x) == id(y)
True
>>> id(y) == id('123')
True
>>> # array.array
>>> import array
>>> array.array('i', [1, 2, 3]) == array.array('i', [1, 2, 3])[:]
True
>>> id(array.array('i', [1, 2, 3])) == id(array.array('i', [1, 2, 3])[:])
False
>>> id(array.array('i', [1, 2, 3])[:]) == id(array.array('i', [1, 2, 3])[:])
False
>>> x = array.array('i', [1, 2, 3])
>>> x[:]
array('i', [1, 2, 3])
>>> x == x[:]
True
>>> id(x) == id(x[:])
False
>>> id(x[:]) == id(x[:])
True
>>> id(x) == id(array.array('i', [1, 2, 3]))
False
>>> id(x[:]) == id(array.array('i', [1, 2, 3]))
True
>>> y = x[:]
>>> id(x) == id(y)
False
>>> id(x[:]) == id(y[:])
True
>>> id(y) == id(array.array('i', [1, 2, 3]))
False
>>> # bytes objects
>>> bytes(123) == bytes(123)[:]
True
>>> id(bytes(123)) == id(bytes(123)[:])
True
>>> id(bytes(123)[:]) == id(bytes(123)[:])
True
>>> x = bytes(123)
>>> x[:]
'123'
>>> x == x[:]
True
>>> id(x) == id(x[:])
True
>>> id(x[:]) == id(x[:])
True
>>> id(x) == id(bytes(123))
False
>>> id(x[:]) == id(bytes(123))
False
>>> y = x[:]
>>> id(x) == id(y)
True
>>> id(x[:]) == id(y[:])
True
>>> id(y) == id(bytes(123))
False
>>> 
