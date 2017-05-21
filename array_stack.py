from array_list import *

#a Stack is an
#Array object with a
#head, the first value of the stack
#and an Array, which is the Array
class Stack:
    def __init__(self, Array):
        self.Array = Array
        self.head = Stack.find_head(self)

    def __eq__(self, other):
        return (type(other) == Stack) and (self.head == other.head) and (self.Array == other.Array)

    def __repr__(self):
        return 'head: {}  Array: {}'.format(self.head, self.Array)

    def find_head(self):
        if length(self.Array) == 0:
            return None
        else:
            return self.Array.array[0]

#returns an empty stack
def empty_stack():
    return Stack(Array([], 0))

#Stack1 is a Stack
#val is an int
#Stack, int --> Stack
#Returns a new stack with val at the front
def push(Stack1, val):
    return Stack(add(Stack1.Array, 0, val))

#Stack1 is a Stack
#Stack --> int
#returns the first value in Stack
def peek(Stack1):
    return Stack1.head

#Stack1 is a Stack
#Stack --> int
#Returns the number of elements in Stack1
def size(Stack1):
    return length(Stack1.Array)

#Stack1 is a Stack
#Stack --> boolean
#returns True if Stack is empty, False otherwise
def is_empty(Stack1):
    return (size(Stack1) == 0)


#Stack1 is a Stack
#Stack --> (int, Stack)
#Returns a tuple with the removed head element and the new Stack without the old head
def pop(Stack1):
    if size(Stack1) == 0:
        raise IndexError('stack is empty')
    else:
        return (Stack1.head, Stack((remove(Stack1.Array, 0)[1])))

