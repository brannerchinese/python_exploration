import array
def test(choice):
    choices = {'list': [1, 2, 3],
            'tuple': (1, 2, 3),
            'string': '123',
            'array': array.array('i', [1, 2, 3]),
            'bytes': bytes(123),
            'buffer': buffer('123'[:]),
            'bytearray': bytearray('123'[:])
            }
    x = choices[choice]
    print id(x[:]) == id(x[:])
    y1 = x[:]
    y2 = x[:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id(x[:])
    print id(x[:])
    print id(x[:])
    print id(x[:])

test('list')
test('array')
test('tuple')
test('string')
test('bytes')
test('buffer')
test('bytearray')

################

def test_list():
    print id([1, 2, 3][:]) == id([1, 2, 3][:])
    y1 = [1, 2, 3][:]
    y2 = [1, 2, 3][:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])

def test_tuple():
    print id((1, 2, 3)[:]) == id((1, 2, 3)[:])
    y1 = (1, 2, 3)[:]
    y2 = (1, 2, 3)[:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id((1, 2, 3)[:])
    print id((1, 2, 3)[:])
    print id((1, 2, 3)[:])
    print id((1, 2, 3)[:])

def test_array():
    print id(array.array('i', [1, 2, 3])[:]) == id(array.array('i', [1, 2, 3])[:])
    y1 = array.array('i', [1, 2, 3])[:]
    y2 = array.array('i', [1, 2, 3])[:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])

def test_string():
    print id('123'[:]) == id('123'[:])
    y1 = '123'[:]
    y2 = '123'[:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id('123'[:])
    print id('123'[:])
    print id('123'[:])
    print id('123'[:])

def test_bytes():
    print id(bytes(123)[:]) == id(bytes(123)[:])
    y1 = bytes(123)[:]
    y2 = bytes(123)[:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id(bytes(123)[:])
    print id(bytes(123)[:])
    print id(bytes(123)[:])
    print id(bytes(123)[:])

test_list()
test_tuple()
test_array()
test_string()
test_bytes()


def test_buffer():
    print id(buffer('123'[:])) == id(buffer('123'[:]))
    y1 = buffer('123'[:])
    y2 = buffer('123'[:])
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id(buffer('123'[:]))
    print id(buffer('123'[:]))
    print id(buffer('123'[:]))
    print id(buffer('123'[:]))


def test_bytearray():
    print id(bytearray('123'[:])) == id(bytearray('123'[:]))
    y1 = bytearray('123'[:])
    y2 = bytearray('123'[:])
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id(bytearray('123'[:]))
    print id(bytearray('123'[:]))
    print id(bytearray('123'[:]))
    print id(bytearray('123'[:]))


test_buffer()
test_bytearray()

################

def test_list2():
    print id([1, 2, 3][:]) == id([1, 2, 3][:])
    y1 = [1, 2, 3][:]
    y2 = [1, 2, 3][:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])
    print id([1, 2, 3][:])

def test_array2():
    print id(array.array('i', [1, 2, 3])[:]) == id(array.array('i', [1, 2, 3])[:])
    y1 = array.array('i', [1, 2, 3])[:]
    y2 = array.array('i', [1, 2, 3])[:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])
    print id(array.array('i', [1, 2, 3])[:])

test_list2()
test_array2()


################

import time
def test_list3():
    print id([1, 2, 3][:]) == id([1, 2, 3][:])
    y1 = [1, 2, 3][:]
    y2 = [1, 2, 3][:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id([1, 2, 3][:])
    time.sleep(.5)
    print id([1, 2, 3][:])
    time.sleep(.5)
    print id([1, 2, 3][:])
    time.sleep(.5)
    print id([1, 2, 3][:])
    time.sleep(.5)
    print id([1, 2, 3][:])
    time.sleep(.5)
    print id([1, 2, 3][:])
    time.sleep(.5)
    print id([1, 2, 3][:])
    time.sleep(.5)
    print id([1, 2, 3][:])

def test_array3():
    print id(array.array('i', [1, 2, 3])[:]) == id(array.array('i', [1, 2, 3])[:])
    y1 = array.array('i', [1, 2, 3])[:]
    y2 = array.array('i', [1, 2, 3])[:]
    print id(y1) == id(y2)
    print id(y1) == id(y1)
    print id(array.array('i', [1, 2, 3])[:])
    time.sleep(.5)
    print id(array.array('i', [1, 2, 3])[:])
    time.sleep(.5)
    print id(array.array('i', [1, 2, 3])[:])
    time.sleep(.5)
    print id(array.array('i', [1, 2, 3])[:])
    time.sleep(.5)
    print id(array.array('i', [1, 2, 3])[:])
    time.sleep(.5)
    print id(array.array('i', [1, 2, 3])[:])
    time.sleep(.5)
    print id(array.array('i', [1, 2, 3])[:])
    time.sleep(.5)
    print id(array.array('i', [1, 2, 3])[:])

test_list3()
test_array3()
