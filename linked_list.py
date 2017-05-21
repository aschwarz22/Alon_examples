#Linked List implementation in python
#Alon Schwarz



# A Linked List contains a
#first, an int and a 
#rest, which is either another Linked list or None
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return (type(other) == Pair) and (self.first == other.first) and (self.rest == other.rest)

    def __repr__(self):
        return ('first: {} rest: {}').format(self.first, self.rest)


#Pair1 is an anylist
#anyList -> int
#Returns the length of the list

def length(Pair1):
    count = 0
    if Pair1 == None or Pair1.first == None:
        return count
    elif Pair1.rest == None:
        return count + 1
    else:
        count += 1 + length(Pair1.rest)
        return count



#returns an empty list
def empty_list():
    return Pair(None, None)

#Pair1 is a Linked List
#index is an int
#value can be a str, int, or float
#adds value at index in Pair1
def add(Pair1, index, value):
    if index == 0 and length(Pair1) == 0:
        return Pair(value, Pair1.rest)
    elif index == 0:
        return Pair(value, Pair(Pair1.first, Pair1.rest))
    elif length(Pair1) < index or index < 0:
        raise IndexError
    elif Pair1.rest == None and index == 1:
        return Pair(Pair1.first, Pair(value, None))
    else:
        return Pair(Pair1.first, add(Pair1.rest, index-1, value))


#Pair1 is a Linked List
#Index is an int
#Finds value at index in Pair1
def get(Pair1, index):
    if length(Pair1) < index or index < 0:
        raise IndexError()
    elif index == 0:
        return Pair1.first
    elif index == 1 and Pair1.rest == None:
        return None
    else:
        return get(Pair1.rest, index-1)


#Pair1 is a Linked List
#index is an int
#value can be a str, int, or float
#sets value at index in Pair1
def set(Pair1, index, value):
    if length(Pair1) <= index or index < 0:
        raise IndexError('Index out of range')
    elif index == 0:
            return Pair(value, Pair1.rest)
    else:
        return Pair(Pair1.first, set(Pair1.rest, index - 1, value))


#Pair1 is a Linked List
#index is an int
#removes value at index in Pair1
def remove(Pair1, index):
    if index > length(Pair1) or index < 0:
        raise IndexError("index not found")
    else:
        count = 0
        previous = None
        current = Pair1
        while count < index:
            count += 1
            previous = current
            current = current.rest
        if index == 0 and length(Pair1) == 1:
            return (Pair1.first, Pair(None, None))
        elif index == 0:
            return (Pair1.first, Pair1.rest)
        else:
            removedValue = previous.first
            previous.rest = current.rest
        return (removedValue, Pair1)




