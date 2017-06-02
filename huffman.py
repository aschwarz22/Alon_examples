import sys
import array_list
from linked_list import *
from huffman_bits_io import *

#an Hnode is a node containing
#a frequency, sum of the frequencies in left and right,
#left, which is another node or leaf
#a right, which is another node or leaf and
#a letternum, the ASCII value of the smallest letter in the (sub)tree
class Hnode:
    def __init__(self, frequency, left, right):
        self.frequency = frequency
        self.left = left
        self.right = right
        self.letternum = gets_letter(self)


    def __eq__(self, other):
        return (type(other) == Hnode) and (self.frequency == other.frequency) and (self.letternum == other.letternum) and (self.left == other.left) and (self.right == other.right)

    def __repr__(self):
        return 'Node: frequency: {}, smallest num: {}'.format(self.frequency, self.letternum)


def gets_letter(node1):
    if node1.left.letternum > node1.right.letternum:
        return node1.right.letternum
    else:
        return node1.left.letternum

#an Hleaf is a node containing
#a letternum, an int representing the ASCII value of a letter
#a frequency, the frequency of the letter
class Hleaf:
    def __init__(self, letternum, frequency):
        self.letternum = letternum
        self.frequency = frequency

    def __eq__(self, other):
        return (type(other) == Hleaf) and (self.letternum == other.letternum) and (self.frequency == other.frequency) and (self.letternum == other.letternum)

    def __repr__(self):
        return 'Leaf: Letter: {}  frequency: {}'.format(self.letternum, self.frequency)


#fname is a str
#str --> list
#returns a list with each letter in str1 and its frequency
def str_to_freq(fname):
    str1 = ''
    length1 = 0
    try:
        f = open(fname, "r")
        #gets string contents of fname into a string
        for line in f:
            for char in line:
                length1 += 1
                str1 += char
    #raises IOError if file isn't found
    except IOError:
        raise IOError("invalid file name")
    #initializes return list
    lista = array_list.Array([0]*256, 256)
    for i in range(length1):
        #goes to next loop if letter has been checked previously
        if str1[i] in str1[:i]:
            continue
        #creates new string to not mutate original
        init_str = str1
        #count counts number of unique characters in init_str
        count = 0
        #runs for every unique charachter in str1
        while str1[i] in init_str:
            #counts 
            newIdx = init_str.index(str1[i])
            count += 1
            #creates new string starting after where the letter was just found
            init_str = init_str[newIdx+1:]
        #adds letter and frequency to lista
        end = lista.length
        if ord(str1[i]) <= 256:
            lista.array[ord(str1[i])] = count
    f.close()
    return lista

#treea is an Hnode or Hleaf
#treeb is an Hnod or Hleaf
#Hnode Hnode --> boolean
#returns True if the ASCII value in treea is less than treeb
#and false otherwise
def comes_before(treea, treeb):
    if treea.frequency == treeb.frequency:
        return treea.letternum < treeb.letternum
    else:
        return treea.frequency < treeb.frequency

#freqlist is an Array
#Array --> linked list
#makes a sorted lnked list holding tuples which
#contain a letter's ASCII value and frequency
def lists_nodes(freqlist):
    Pair1 = Pair(None, None)
    for i in range(256):
        if freqlist.array[i] != 0:
            newleaf = Hleaf(i, freqlist.array[i])
            Pair1 = insert_sorted(Pair1, newleaf, comes_before)
    return Pair1

#nodesList is a linked list
#linked list --> Hnode
#returns a huffman tree made from nodes in nodesList
def make_tree(nodesList):
    lista = nodesList
    while lista.rest is not None:
        #left subtree is the lowest frequency node in the sorted nodes list
        left = lista.first
        #removes left from sorted nodes list
        lista = lista.rest
        #right subtree is the new lowest frequency/ascii node in the sorted nodes list
        right = lista.first
        #removes right from sorted nodes list
        lista = lista.rest
        #combines frequency of two removed nodes and makes it the frequency of the new node
        newfreq = left.frequency + right.frequency
        newNode = Hnode(newfreq, left, right)
        #inserts newNode into sorted nodes list
        lista = insert_sorted(lista, newNode, comes_before)
    return lista.first

#t1 is a node
#code is a str
#creates a generator which yields each character in t1 and its code
def prefix_iterator(t1, code = ''):
    if t1 is Hleaf or Hnode:
        if isinstance(t1, Hleaf):
            yield (chr(t1.letternum), code)
        else:
            #recurses to left subtree and adds '0' to the code
            yield from prefix_iterator(t1.left, code + '0')
            #recurses to right subtree and adds '1' to the code
            yield from prefix_iterator(t1.right, code + '1')


#a is a character
#b is a character
#returns True if the ASCII value of a is less than that of b
#and returns false otherwise
def comes_before_ascii(a, b):
    return ord(a[0]) < ord(b[0])

#t1 is a node
#node --> linked list
#sorts individual nodes based on ASCII values and returns them in a linked list
def sort_codes(t1):
    generator = prefix_iterator(t1, '')
    Pair1 = Pair(None, None)
    #adds code and ascii to a sorted linked list
    for i in generator:
        Pair1 = insert_sorted(Pair1, i, comes_before_ascii)
    return Pair1

#ar1 is an Array
#Pair1 is a linked list
#Array linked list --> array
#returns array with tuples holding
#the ASCII value of a letter,
#the frequency of the letter and
#the huffman code of each character
def ascii_code_freq(ar1, Pair1):
    newArray = array_list.Array([0] * 256, 256)
    for x in range(length(Pair1)):
        temp = ord(Pair1.first[0])
        for x in range(ar1.length):
            if x == temp:
                temp2 = ar1.array[x]
                newArray.array[x] = (Pair1.first[1], temp2)
        Pair1 = Pair1.rest
    return newArray

#infile is a str
#str --> str
#returns the original string in the infile file
def line_generator(infile):
    f = open(infile, "r")
    str1 = ''
    for line in f:
        for char in line:
            str1 += char
    f.close()
    return str1

#t1 is a node
#makes a generator which holds the characters in t1 from left to right
def gets_leaf_letters(t1):
    if t1 is Hleaf or Hnode:
        if isinstance(t1, Hleaf):
            yield (chr(t1.letternum))
        else:
            yield from prefix_iterator(t1.left)
            yield from prefix_iterator(t1.right)

#infile is a str
#outfile is a str
#writes the huffman code for the contents in infile and
#writes it to outfile
def huffman_encode(infile, outfile):
    hb_writer = HuffmanBitsWriter(outfile)
    freqArr = str_to_freq(infile)
    nodesList = lists_nodes(freqArr)
    t1 = make_tree(nodesList)
    lettersnum = length(nodesList)
    if lettersnum == 0:
        hb_writer.write_byte(lettersnum)
        return ""
    else:
        codesList = sort_codes(t1)
        freqCodeArr = ascii_code_freq(freqArr, codesList)
        hb_writer.write_byte(length(nodesList))
        str1 = line_generator(infile)
        headerLen = length(codesList)
        for x in range(freqCodeArr.length):
            if freqCodeArr.array[x]!= 0:
                hb_writer.write_byte(x)
                hb_writer.write_int(freqArr.array[x])
        emptyString = ""
        for i in str1:
            temp = ord(i)
            if temp <= 256:
                huffmanCode = freqCodeArr.array[temp][0]
            emptyString += huffmanCode
        hb_writer.write_code(emptyString)
        hb_writer.close()
        newstr = ''
        for i in gets_leaf_letters(t1):
            newstr += i[0]
        return newstr

#outfile is a str
#str1 is a str
#writes str1 to outfile
def write_to_file(outfile, str1):
    f = open(outfile, "w")
    f.write(str1)
    f.close()

#readfile is a str
#writefile is a str
#decodes the compressed contents of readfile and
#writes it into writefile
def huffman_decode(readfile, writefile):
    hb_reader = HuffmanBitsReader(readfile)
    try:
        totalLetters = hb_reader.read_byte()
        freqArr = array_list.Array([0]*256, 256)
        for x in range(0, totalLetters):
            newASCII = hb_reader.read_byte()
            newFreq = hb_reader.read_int()
            freqArr.array[newASCII] = newFreq
        nodesList = lists_nodes(freqArr)
        t1 = make_tree(nodesList)
        count = 0
        newtree = t1
        chars = t1.frequency
        str1 = ''
        while chars != 0:
            if type(newtree) == Hleaf:
                str1 += chr(newtree.letternum)
                chars -= 1
                newtree = t1
            else:
                hbit = hb_reader.read_bit()
                if hbit is True:
                    newtree = newtree.right
                else:
                    newtree = newtree.left
        hb_reader.close()
        if str1 == '':
            hb_reader.close()
            return None
        write_to_file(writefile, str1)
    except:
        hb_reader.close()
        return None


import unittest

class TestCase(unittest.TestCase):
    def test_leaf(self):
        l1 = Hleaf(32, 3)
        l2 = Hleaf(97, 4)
        l3 = Hleaf(32, 3)
        self.assertEqual(l1.letternum, 32)
        self.assertEqual(l2.letternum, 97)
        self.assertEqual(l2.frequency, 4)
        self.assertEqual(l1.frequency, 3)
        self.assertEqual(l1, l3)
        self.assertEqual(print(l1), None)

    def test_node(self):
        right = Hleaf(5, 5)
        left = Hleaf(40, 2)
        node1 = Hnode(7, left, right)
        node2 = Hnode(2, Hleaf(15, 1), Hleaf(32, 1))
        node3 = Hnode(7, Hleaf(40, 2), Hleaf(5, 5))
        self.assertEqual(node1, node3)
        self.assertEqual(node1.letternum, 5)
        self.assertEqual(node2.letternum, 15)
        self.assertEqual(node1.frequency, 7)
        self.assertEqual(node2.frequency, 2)
        self.assertEqual(node1.right, Hleaf(5, 5))
        self.assertEqual(node2.left, Hleaf(15, 1))
        self.assertEqual(print(node1), None)


    def test_str_fail(self):
        with self.assertRaises(IOError):
            str_to_freq('a')

    def test_encode(self):
        self.assertEqual(huffman_encode('sample.txt', 'output.bin'), 'a')

    def test_encode_again(self):
         self.assertEqual(huffman_encode('txt.txt', 'outfile.bin'), ' bdca')
         self.assertEqual(huffman_encode('sample2.txt', 'new1.bin'), "lwbm\nr,gpy-faestuAcohidnk'FL.PWYvT ")
         self.assertEqual(huffman_encode('empty.txt', 'new1.bin'), "")

    def test_decode(self):
        self.assertEqual(huffman_decode('outfile.bin', 'new.txt'), None)
        self.assertEqual(huffman_decode('new1.bin', 'out1.txt'), None)

    def test_comes_before(self):
        treea = Hleaf(7, 2)
        treeb = Hleaf(98, 3)
        self.assertTrue(comes_before(treea, treeb))
        self.assertFalse(comes_before(treeb, treea))

    def test_Array(self):
        Array1 = array_list.Array([1, 2, 3, 4], 4)
        Array2 = array_list.Array(['Oregon', 'Washington', 'California'], 3)
        Array3 = array_list.Array([1, 2, 3, 4], 4)
        self.assertEqual(Array1.array, [1, 2, 3, 4])
        self.assertEqual(Array2.array, ['Oregon', 'Washington', 'California'])
        self.assertEqual(Array1.length, 4)
        self.assertEqual(Array2.length, 3)
        self.assertTrue(Array1 == Array3)
        self.assertEqual(print(Array1), None)

    def test_list(self):
        Pair1 = Pair(1, Pair(2, Pair(3, None)))
        Pair2 = Pair(None, None)
        Pair3 = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(Pair1.first, 1)
        self.assertEqual(Pair1.rest, Pair(2, Pair(3, None)))
        self.assertTrue(Pair1 == Pair3)
        self.assertEqual(print(Pair2), None)

    def test_length(self):
        Pair1 = Pair(None, None)
        f1 = length(Pair(1, None))
        Pair2 = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(length(Pair1), 0)
        self.assertEqual(length(Pair2), 3)

    def test_add(self):
        f1 = add(Pair(None, None), 0, 1)
        f2 = add(Pair(1, None), 0, 88)
        f3 = add(Pair(1, None), 1, 88)
        f4 = add(Pair(1, Pair(2, Pair(4, Pair(5, Pair(6, None))))), 2, 3)
        self.assertEqual(f1, Pair(1, None))
        self.assertEqual(f2, Pair(88, Pair(1, None)))
        self.assertEqual(f3, Pair(1, Pair(88, None)))
        self.assertEqual(f4, Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, Pair(6, None)))))))
        with self.assertRaises(IndexError):
            add(Pair(1, None), -1, 1)


if __name__ == '__main__':
    unittest.main()


