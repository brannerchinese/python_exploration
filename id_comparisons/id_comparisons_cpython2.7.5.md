~~~
In [1]: [1, 2, 3] == [1, 2, 3][:]
Out[1]: True

In [2]: id([1, 2, 3]) == id([1, 2, 3][:])
Out[2]: False

In [3]: x = [1, 2, 3]

In [4]: x[:]
Out[4]: [1, 2, 3]

In [5]: x == x[:]
Out[5]: True

In [6]: id(x) == id(x[:])
Out[6]: False

In [7]: id(x) == id([1, 2, 3])
Out[7]: False

# So far, illustrates that a slice of a list is a different object from the list, even when its __repr__ is identical to the list's __repr__.

# But why this:

In [8]: id(x[:]) == id([1, 2, 3])
Out[8]: True

# ?
David Prager Branner brannerchinese@gmail.com
	
10:53 PM (13 hours ago)
		
Reply
to Thomas, Allison
Ahoy!

Three more interesting developments to report.

First, if (for the same kind of list as above) I assign x[:] to a variable y, I get slightly different results (boldfaced):

In [9]: y = x[:]

In [10]: id(x) == id(y)
Out[10]: False

In [11]: id(y) == id([1, 2, 3])
Out[11]: False

Second, the results with a tuple are somewhat different from those of a list (boldfaced items are different):

In [1]: (1, 2, 3) == (1, 2, 3)[:]
Out[1]: True

In [2]: id((1, 2, 3)) == id((1, 2, 3)[:])
Out[2]: False

In [3]: x = (1, 2, 3)

In [4]: x[:]
Out[4]: (1, 2, 3)


In [5]: x == x[:]
Out[5]: True

In [6]: id(x) == id(x[:])
Out[6]: True

In [7]: id(x) == id((1, 2, 3))
Out[7]: False

In [8]: id(x[:]) == id((1, 2, 3))
Out[8]: False

In [9]: y = x[:]

In [10]: id(x) == id(y)
Out[10]: True

In [11]: id(y) == id((1, 2, 3))
Out[11]: False

Third, the high-level expected behavior (True in all cases) does obtain when the sequence in question is a string (boldfaced if different from list):

In [1]: '123' == '123'[:]
Out[1]: True

In [2]: id('123') == id('123'[:])
Out[2]: True

In [3]: x = '123'

In [4]: x[:]
Out[4]: '123'

In [5]: x == x[:]
Out[5]: True

In [6]: id(x) == id(x[:])
Out[6]: True

In [7]: id(x) == id('123')
Out[7]: True

In [8]: id(x[:]) == id('123')
Out[8]: True

In [9]: y = x[:]

In [10]: id(x) == id(y)
Out[10]: True

In [11]: id(y) == id('123')
Out[11]: True

# array.array

In [1]: array.array('i', [1, 2, 3]) == array.array('i', [1, 2, 3])[:]
Out[1]: True

In [2]: id(array.array('i', [1, 2, 3])) == id(array.array('i', [1, 2, 3])[:])
Out[2]: False

In [3]: x = array.array('i', [1, 2, 3])

In [4]: x[:]
Out[4]: array('i', [1, 2, 3])

In [5]: x == x[:]
Out[5]: True

In [6]: id(x) == id(x[:])
Out[6]: False

In [7]: id(x) == id(array.array('i', [1, 2, 3]))
Out[7]: False

In [8]: id(x[:]) == id(array.array('i', [1, 2, 3]))
Out[8]: True

In [9]: y = x[:]

In [10]: id(x) == id(y)
Out[10]: False

In [11]: id(y) == id(array.array('i', [1, 2, 3]))
Out[3112]: False

# bytes objects

In [1]: bytes(123) == bytes(123)[:]
Out[1]: True

In [2]: id(bytes(123)) == id(bytes(123)[:])
Out[2]: True

In [3]: x = bytes(123)

In [4]: x[:]
Out[4]: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

In [5]: x == x[:]
Out[5]: True

In [6]: id(x) == id(x[:])
Out[6]: True

In [7]: id(x) == id(bytes(123))
Out[7]: False

In [8]: id(x[:]) == id(bytes(123))
Out[8]: False

In [9]: y = x[:]

In [10]: id(x) == id(y)
Out[10]: True

In [11]: id(y) == id(bytes(123))
Out[11]: False
~~~