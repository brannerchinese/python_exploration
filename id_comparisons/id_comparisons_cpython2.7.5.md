Python 2.7.5 (default, Aug 31 2013, 07:00:49) 
Type "copyright", "credits" or "license" for more information.

IPython 1.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import array

In [2]: # list

In [3]: [1, 2, 3] == [1, 2, 3][:]
Out[3]: True

In [4]: id([1, 2, 3]) == id([1, 2, 3][:])
Out[4]: False

In [5]: x = [1, 2, 3]

In [6]: x[:]
Out[6]: [1, 2, 3]

In [7]: x == x[:]
Out[7]: True

In [8]: id(x) == id(x[:])
Out[8]: False

In [9]: id(x) == id([1, 2, 3])
Out[9]: False

In [10]: id(x[:]) == id([1, 2, 3])
Out[10]: True

In [11]: y = x[:]

In [12]: id(x) == id(y)
Out[12]: False

In [13]: id(y) == id([1, 2, 3])
Out[13]: False

In [14]: # tuple

In [15]: (1, 2, 3) == (1, 2, 3)[:]
Out[15]: True

In [16]: id((1, 2, 3)) == id((1, 2, 3)[:])
Out[16]: False

In [17]: x = (1, 2, 3)

In [18]: x[:]
Out[18]: (1, 2, 3)

In [19]: x == x[:]
Out[19]: True

In [20]: id(x) == id(x[:])
Out[20]: True

In [21]: id(x) == id((1, 2, 3))
Out[21]: False

In [22]: id(x[:]) == id((1, 2, 3))
Out[22]: False

In [23]: y = x[:]

In [24]: id(x) == id(y)
Out[24]: True

In [25]: id(y) == id((1, 2, 3))
Out[25]: False

In [26]: # string

In [27]: '123' == '123'[:]
Out[27]: True

In [28]: id('123') == id('123'[:])
Out[28]: True

In [29]: x = '123'

In [30]: x[:]
Out[30]: '123'

In [31]: x == x[:]
Out[31]: True

In [32]: id(x) == id(x[:])
Out[32]: True

In [33]: id(x) == id('123')
Out[33]: True

In [34]: id(x[:]) == id('123')
Out[34]: True

In [35]: y = x[:]

In [36]: id(x) == id(y)
Out[36]: True

In [37]: id(y) == id('123')
Out[37]: True

In [38]: # array.array

In [39]: array.array('i', [1, 2, 3]) == array.array('i', [1, 2, 3])[:]
Out[39]: True

In [40]: id(array.array('i', [1, 2, 3])) == id(array.array('i', [1, 2, 3])[:])
Out[40]: False

In [41]: x = array.array('i', [1, 2, 3])

In [42]: x[:]
Out[42]: array('i', [1, 2, 3])

In [43]: x == x[:]
Out[43]: True

In [44]: id(x) == id(x[:])
Out[44]: False

In [45]: id(x) == id(array.array('i', [1, 2, 3]))
Out[45]: False

In [46]: id(x[:]) == id(array.array('i', [1, 2, 3]))
Out[46]: True

In [47]: y = x[:]

In [48]: id(x) == id(y)
Out[48]: False

In [49]: id(y) == id(array.array('i', [1, 2, 3]))
Out[49]: False

In [50]: # bytes objects

In [51]: bytes(123) == bytes(123)[:]
Out[51]: True

In [52]: id(bytes(123)) == id(bytes(123)[:])
Out[52]: True

In [53]: x = bytes(123)

In [54]: x[:]
Out[54]: '123'

In [55]: x == x[:]
Out[55]: True

In [56]: id(x) == id(x[:])
Out[56]: True

In [57]: id(x) == id(bytes(123))
Out[57]: False

In [58]: id(x[:]) == id(bytes(123))
Out[58]: False

In [59]: y = x[:]

In [60]: id(x) == id(y)
Out[60]: True

In [61]: id(y) == id(bytes(123))
Out[61]: False
