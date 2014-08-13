~~~
Jython 2.7b2 (default:a5bc0032cf79+, Apr 22 2014, 21:20:17) 
[Java HotSpot(TM) 64-Bit Server VM (Oracle Corporation)] on java1.7.0_51
Type "help", "copyright", "credits" or "license" for more information.
>>> [1, 2, 3] == [1, 2, 3][:] 
True
>>> id([1, 2, 3]) == id([1, 2, 3][:])
False
>>> x = [1, 2, 3]
>>> x[:]
[1, 2, 3]
>>> x == x[:]
True
>>> id(x) == id(x[:])
False
>>> id(x[:]) == id(x[:])
False
>>> id(x) == id([1, 2, 3])
False
>>> id(x[:]) == id([1, 2, 3])
False
>>> y = x[:]
>>> id(x) == id(y)
False
>>> id(x[:]) == id(y[:])
False
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
>>> (1, 2, 3)
(1, 2, 3)
>>> x == x[:]
True
>>> id(x) == id(x[:])
False
>>> id(x[:]) == id(x[:])
False
>>> id(x) == id((1, 2, 3))
False
>>> id(x[:]) == id((1, 2, 3))
False
>>> y = x[:]
>>> id(x) == id(y)
False
>>> id(x[:]) == id(y[:])
False
>>> id(y) == id((1, 2, 3))
False
>>> # Strings
>>> '123' == '123'[:]
True
>>> id('123') == id('123'[:])
False
>>> id('123'[:]) == id('123'[:])
False
>>> x = '123'
>>> x[:]
'123'
>>> '123'
'123'
>>> x == x[:]
True
>>> id(x) == id(x[:])
False
>>> id(x) == id('123')
False
>>> id(x[:]) == id(x[:])
False
>>> id(x[:]) == id('123')
False
>>> y = x[:]
>>> id(x) == id(y)
False
>>> id(y) == id('123')
False
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
False
>>> id(x) == id(array.array('i', [1, 2, 3]))
False
>>> id(x[:]) == id(array.array('i', [1, 2, 3]))
False
>>> y = x[:]
>>> id(x) == id(y)
False
>>> id(x[:]) == id(y[:])
False
>>> id(y) == id(array.array('i', [1, 2, 3]))
False
>>> # bytes objects
>>> bytes(123) == bytes(123)[:]
True
>>> id(bytes(123)) == id(bytes(123)[:])
False
>>> id(bytes(123)[:]) == id(bytes(123)[:])
False
>>> x = bytes(123)
>>> x[:]
'123'
>>> x == x[:]
True
>>> id(x) == id(x[:])
False
>>> id(x[:]) == id(x[:])
False
>>> id(x) == id(bytes(123))
False
>>> id(x[:]) == id(bytes(123))
False
>>> y = x[:]
>>> id(x) == id(y)
False
>>> id(x[:]) == id(y[:])
False
>>> id(y) == id(bytes(123))
False
~~~