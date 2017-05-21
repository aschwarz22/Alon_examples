from array_list import *
import unittest

class TestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(empty_list(), Array([], 0))

    def test_Array(self):
        Array1 = Array([1, 2, 3, 4], 4)
        Array2 = Array(['Oregon', 'Washington', 'California'], 3)
        Array3 = Array([1, 2, 3, 4], 4)
        self.assertEqual(Array1.array, [1, 2, 3, 4])
        self.assertEqual(Array2.array, ['Oregon', 'Washington', 'California'])
        self.assertEqual(Array1.length, 4)
        self.assertEqual(Array2.length, 3)
        self.assertTrue(Array1 == Array3)

    def test_splice(self):
        Array1 = Array([1.3, 3.5, 3.2], 3)
        Array2 = Array([1.2], 1)
        self.assertEqual(splice(Array1, 0, 2).array, [1.3, 3.5])
        self.assertEqual(splice(Array2, 0, 1).array, [1.2])

    def test_length(self):
        Array1 = Array([], 0)
        Array2 = Array([1, 2, 3], 3)
        self.assertEqual(length(Array1), 0)
        self.assertEqual(length(Array2), 3)

    def test_add(self):
        Array1 = Array([100, 200, 300, 500], 4)
        Array2 = Array(['John', 'Orange'], 2)
        func1 = add(Array1, 3, 400)
        func2 = add(Array1, 0, 'Green')
        self.assertEqual(func1, Array([100, 200, 300, 400, 500], 5))

    def test_get(self):
        arr1 = Array([3, 4], 2)
        arr2 = Array(['phone'], 1)
        f1 = get(arr1, 1)
        f2 = get(arr2, 0)
        self.assertEqual(f1, 4)
        self.assertEqual(f2, 'phone')

    def test_set(self):
        f1 = set(Array([10, 20, 35, 40], 4), 2, 30)
        f2 = set(Array(['muffin', 'bagel', 'croissant'], 3), 2, 'juice')
        self.assertEqual(f1.array, [10, 20, 30, 40])
        self.assertEqual(f2.array, ['muffin', 'bagel', 'juice'])

    def test_remove(self):
        f1 = remove(Array([1, 2, 3, 3, 4, 5], 6), 3)
        self.assertEqual(f1, (3, Array([1, 2, 3, 4, 5], 5)))
        with self.assertRaises(IndexError):
            remove(Array(['Orange', 'Blue', 'cup', 'Green'], 4), -1)
if __name__ == '__main__':
    unittest.main()
