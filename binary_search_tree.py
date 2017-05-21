#binary search tree implementation



#A BstTree is a
#Binary Tree with
#a data,
#a left which is None or another BstTree
#or a right which is None or another BstTree
class Tree:
    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.data = data

    def __eq__(self, other):
        return (type(other) == Tree) and (self.left == other.left) and (self.right == other.right)

    def __repr__(self):
        return ('Tree({}, {}, {})'.format(self.data, self.left, self.right))

#returns an empty BstTree
def is_empty():
    return Tree(None, None, None)

#Tree1 is a bstTree
#val is an int
#BstTree, int --> BstTree
#Inserts value at location
def insert(Tree1, val):
    if Tree1.data != None:
        if val < Tree1.data:
            if Tree1.left is None:
                Tree1.left = Tree(val, None, None)
            else:
                insert(Tree1.left, val)
        elif val > Tree1.data:
            if Tree1.right is None:
                Tree1.right = Tree(val, None, None)
            else:
                insert(Tree1.right, val)
    else:
        Tree1.data = val
    return Tree1

#Tree1 is a BstTree
#val is an int
#BstTree, int --> Boolean
#Returns True if value is in the tree, false otherwise
def lookup(Tree1, val):
    if Tree1.data == None:
        return False
    if val < Tree1.data:
        if Tree1.left is None:
            return False
        return lookup(Tree1.left, val)
    elif val > Tree1.data:
        if Tree1.right is None:
            return False
        return lookup(Tree1.right, val)
    else:
        return True

#Tree1 is a bstTree
#bstTree --> int
#returns minimum value in Tree1
def find_last_left(Tree1):
    if Tree1.left == None:
        val = Tree1.data
    while Tree1 != None:
        val = Tree1.data
        Tree1 = Tree1.left
    return val

#Tree1 is a bstTree
#produces a generator from Tree1 in prefix order (root --> left --> right)
def prefix_iterator(Tree1):
    if Tree1 is not None:
        yield Tree1.data
        yield from prefix_iterator(Tree1.left)
        yield from prefix_iterator(Tree1.right)

#Tree1 is a bstTree
#produces a generator from Tree1 in postfix order (left --> right --> root)
def postfix_iterator(Tree1):
    if Tree1 is not None:
        yield from postfix_iterator(Tree1.left)
        yield from postfix_iterator(Tree1.right)
        yield Tree1.data

#Tree1 is a bstTree
#produces a generator from Tree1 in infix order (left --> root --> right)
def infix_iterator(Tree1):
    if Tree1 is not None:
        yield from infix_iterator(Tree1.left)
        yield Tree1.data
        yield from infix_iterator(Tree1.right)


#Tree1 is a bstTree
#val is an int
#bstTree, int --> bstTree
#removes val in Tree1
def delete(Tree1, val):
    if not lookup(Tree1, val):
        return ('value not found')
    elif Tree1 != None:
        if Tree1.data == val and Tree1.right == None and Tree1.left == None:
            return None
        elif Tree1.data == val and Tree1.right == None:
            #Tree1.data = Tree1.left.data
            #has_children(Tree1)
            return Tree(Tree1.left.data, Tree1.left.left, Tree1.left.right)
        elif Tree1.data == val and Tree1.left == None:
            #Tree1.data = Tree1.right.data
            #has_children(Tree1)
            return Tree(Tree1.right.data, Tree1.right.left, Tree1.right.right)
        elif Tree1.data == val:
            newval = find_last_left(Tree1.right)
            right = delete(Tree1.right, newval)
            return Tree(newval, Tree1.left, right)
        else:
            if val > Tree1.data:
                return Tree(Tree1.data, Tree1.left, delete(Tree1.right, val))
            elif val < Tree1.data:
                return Tree(Tree1.data, delete(Tree1.left, val), Tree1.right)

