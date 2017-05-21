#unittest for array stack implementation

from array_stack import *
import unittest

class TestCase(unittest.TestCase):
    def test_stack(self):
        Stack1 = Stack(Array([1, 2, 3], 3))
        Stack2 = Stack(Array([1, 2, 3], 3))
        Stack3 = Stack(Array([5], 1))
        Stack4 = Stack(Array([], 0))
        self.assertEqual(Stack1.head, 1)
        self.assertEqual(Stack3.head, 5)
        self.assertEqual(Stack1.Array, Array([1, 2, 3], 3))
        self.assertEqual(Stack3.Array, Array([5], 1))
        self.assertTrue(Stack1 == Stack2)
        self.assertEqual(print(Stack1), None)
        self.assertEqual(Stack4.head, None)

    def test_empty(self):
        Stack1 = empty_stack()
        self.assertEqual(Stack1, Stack(Array([], 0)))

    def test_push(self):
        f1 = push(Stack(Array([], 0)), 1)
        f2 = push(Stack(Array([1], 1)), 12)
        self.assertEqual(f1, Stack(Array([1], 1)))
        self.assertEqual(f2, Stack(Array([12, 1], 2)))

    def test_peek(self):
        f1 = peek(Stack(Array([], 0)))
        f2 = peek(Stack(Array([1], 1)))
        self.assertEqual(f1, None)
        self.assertEqual(f2, 1)

    def test_size(self):
        f1 = size(Stack(Array([], 0)))
        f2 = size(Stack(Array([1, 2, 3, 4], 4)))
        self.assertEqual(f1, 0)
        self.assertEqual(f2, 4)

    def test_is_empty(self):
        f1 = is_empty(Stack(Array([], 0)))
        f2 = is_empty(Stack(Array([1], 1)))
        self.assertTrue(f1)
        self.assertFalse(f2)

    def test_pop(self):
        f1 = pop(Stack(Array([1, 2, 3], 3)))
        self.assertEqual(f1, (1, Stack(Array([2, 3], 2))))
        with self.assertRaises(IndexError):
            pop(Stack(Array([], 0)))


    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        print (test_stack.Array.length)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)

if __name__ == '__main__':
    unittest.main()
