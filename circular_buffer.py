from array_list import *

cap = 5000

#a Circular buffer is a
#list object containing a
#headIdx, an int, 
#a tailIdx, an int, and
#a length, an int
class CircleQueue:
    def __init__(self, list, headIdx, tailIdx):
        self.list = list
        self.headIdx = headIdx
        self.tailIdx = tailIdx
        self.length = 0

    def __eq__(self, other):
        return (type(other) == CircleQueue) and (other.list == self.list) and (self.headIdx == other.headIdx) and (self.tailIdx == other.tailIdx)

    def __repr__(self):
        return 'Array: {}\nfirst: {}\n last: {}'.format(self.list, self.headIdx, self.tailIdx)



#Returns an empty Queue
def empty_queue():
    newQueue = CircleQueue([[]]*cap, None, None)
    return newQueue

#CircleQueue1 is a Circlular Buffer
#Circular Buffer --> Boolean
#returns True if the length of CircleQueue1 is 0
def is_empty(CircleQueue1):
    return CircleQueue1.length == 0

#CircleQueue1 is a Circular Buffer
#Circular Buffer --> Boolean
#returns True of the length of CircleQueue1 is equal to the capacity
def is_full(CircleQueue1):
    return size(CircleQueue1) == cap

#CircleQueue1 is a Circular buffer
#val is an int
#Circular buffer, int --> Circular Buffer
#Returns CircleQueue1 with val at the front
def enqueue(CircleQueue1, val):
    #raises Indexerror if buffer is full
    if is_full(CircleQueue1):
        raise IndexError('Queue is full')
    #returns list with element val at index 0 if the buffer isempty
    elif is_empty(CircleQueue1):
        CircleQueue1.list[0] = val
        newQueue = CircleQueue(CircleQueue1.list, 0, 0)
        newQueue.length += 1
        return newQueue
    else:
        #calculates new tail idx (adds one to original index modulus the capacity)
        newTailIdx = (CircleQueue1.tailIdx + 1) % cap

        CircleQueue1.list[newTailIdx] = val
        newl = CircleQueue1.length + 1
        newQueue =  CircleQueue(CircleQueue1.list, CircleQueue1.headIdx, newTailIdx )
        newQueue.length = newl
        return newQueue

#CircleQueue1 is a Circular Buffer
#Circular Buffer --> Circular Buffer
#returns CircularQueue1 without the last element
def dequeue(CircleQueue1):
    if is_empty(CircleQueue1):
        raise IndexError('Queue is empty')
    if CircleQueue1.length == 1:
        return empty_queue()
    else:
        newlist = CircleQueue1.list
        newHeadIdx = (CircleQueue1.headIdx + 1)% cap
        newlist[(newHeadIdx - 1)%cap] = []
        newQueue = CircleQueue(newlist, newHeadIdx, CircleQueue1.tailIdx)
        newQueue.length = CircleQueue1.length - 1
        return newQueue

#CircleQueue1 is a Circular Buffer
#CIrcular Buffer --> int
#returns first value in CircleQueue1
def peek(CircleQueue1):
    if is_empty(CircleQueue1):
        raise IndexError('Queue is empty')
    else:
        return CircleQueue1.list[CircleQueue1.headIdx]

#CircleQueue1 is a Circular buffer
#Circular Buffer --> int
#returns number of elements in CircleQueue1
def size(CircleQueue1):
    return CircleQueue1.length

