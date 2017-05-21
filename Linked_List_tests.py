from linked_list import *
import unittest

class TestCase(unittest.TestCase):
    def test_list(self):
        Pair1 = Pair(1, Pair(2, Pair(3, None)))
        Pair2 = Pair(None, None)
        Pair3 = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(Pair1.first, 1)
        self.assertEqual(Pair1.rest, Pair(2, Pair(3, None)))
        self.assertTrue(Pair1 == Pair3)
        self.assertEqual(print (Pair2), None)

    def test_empty(self):
        Pair1 = empty_list()
        self.assertEqual(Pair1, Pair(None, None))

    def test_length(self):
        Pair1 = Pair(None, None)
        f1 = length(Pair(1, None))
        Pair2 = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(length(Pair1), 0)
        self.assertEqual(length(Pair2), 3)
       
    def test_get(self):
        f1 = get(Pair(4, Pair(5, Pair(3, None))), 1)
        f2 = get(Pair('cat', None), 0)
        self.assertEqual(get(Pair(1, Pair(2, Pair(3, None))), 0), 1)
        self.assertEqual(f1, 5)
        self.assertEqual(f2, 'cat')
        self.assertEqual(get(Pair('cat', None), 1), None)
        with self.assertRaises(IndexError):
            get(Pair(None, None), -1)

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

    def test_set(self):
        f1 = set(Pair(2, Pair(3, Pair(4, None))), 0, 1)
        f2 = set(Pair(1, Pair(2, None)), 1, 88)
        f3 = set(Pair(1, Pair(2, Pair(3, Pair(3, Pair(4, Pair(5, None)))))), 2, 88)
        self.assertEqual(f1, Pair(1, Pair(3, Pair(4, None))))
        self.assertEqual(f2, Pair(1, Pair(88, None)))
        self.assertEqual(f3, Pair(1, Pair(2, Pair(88, Pair(3, Pair(4, Pair(5, None)))))))
        with self.assertRaises(IndexError):
            set(Pair(None, None), -1, 1)

    def test_remove(self):
        f1 = remove(Pair(1, Pair(2, Pair(3, Pair(3, Pair(4, None))))), 3)
        f2 = remove(Pair(1, None), 0)
        f3 = remove(Pair(1, Pair(2, Pair(3, None))), 0)
        self.assertEqual(f1, (3, Pair(1, Pair(2, Pair(3, Pair(4, None))))))
        self.assertEqual(f2, (1, Pair(None, None)))
        self.assertEqual(f3, (1, Pair(2, Pair(3, None))))
        with self.assertRaises(IndexError):
            remove(Pair(None, None), -1)

if __name__ == '__main__':
    unittest.main()
