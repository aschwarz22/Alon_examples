#an Array is
#a list containing an
#array, which is a list
#and length which is an int
class Array:
    def __init__(self, array, length):
        self.array = array
        self.length = length

    def __eq__(self, other):
        return (type(other) == Array) and self.array == other.array and self.length == other.length

    def __repr__(self):
        return ('array: {!r}\n length: {!r}\n').format(self.array, self.length)

#returns an empty Array
def empty_list():
    return Array([], 0)

#a is an Array
#returns number of elements in a
def length(a):
    return a.length

#a is an Array
#first is an int
#last is an int
#Array in int --> Array
#Returns subArray from first to last elements in a
def splice(a, first, last):
    #creates a new element the size of desired splice
    newList = Array(['']*(last-first), last-first)
    count = 0
    for i in range (first, last):
        #maps a values in splice range to newList
        newList.array[count] = a.array[i]
        count += 1
    return newList

#a is ian Array
#index is an int
#val is an int
#Array int int --> Array
#returns a new Array with val at index of the Array
def add(a, index, val):
    #checks if index is valid
    if index > a.length or index < 0:
        raise IndexError("index out of range")
    #creates a new array one element larger than a
    newArray = Array(['']*(a.length + 1), a.length + 1)
    #sets element at index of newArray to val
    newArray.array[index] = val
    i = 0
    count = 0
    while i < a.length:
        #skips over index element in newArray since it was already assigned
        if i == index:
            count += 1
        #maps a values to newArray 
        newArray.array[count] = a.array[i]
        i += 1
        count += 1
    return newArray


#a is an Array
#index is an int
#Array int --> int
#returns value at index of a
def get(a, index):
    #checks if index is valid
    if index > a.length - 1 or index < 0:
        raise IndexError('Index out of range')
    return a.array[index]

#a is an Array
#index is an int
#val is an int
#Array int int --> Array
#sets element at index of a to val
def set(a, index, val):
    #checks if index is valid
    if index > a.length-1 or index < 0:
        raise IndexError("Index out of range")
    #creates a new Array the size of a
    newList = Array(['']*a.length, a.length)
    for i in range(a.length):
        #maps a to newList
        newList.array[i] = a.array[i]
        #sets value at index to val
        if i == index:
            newList.array[i] = val
    return newList

#a is an Array
#index is an int
#a int --> Array
#returns a tuple containing removed element in a at index and
#a new Array without an element at index
def remove(a, index):
    #checks if index is valid
    if index > a.length-1 or index < 0:
        raise IndexError("Index out of range")
    #creates a new empty Array one element small than a
    newList = Array(['']*(a.length-1), a.length-1)
    count = 0
    #if a has one element, return an empty Array
    if a.length == 1:
        return (a.array[0], Array([], 0))
    for i in range (a.length-1):
        #assigns index value to variable val and skips to the next element in a
        if i == index:
            val = a.array[i]
            count += 1
        #maps value at a to the corresponding index in newList
        newList.array[i] = a.array[count]
        count += 1
    return (val, newList)

