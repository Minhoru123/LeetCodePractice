import unittest
from dynamic_design_array import DynamicArray

class TestDynamicArray(unittest.TestCase):
    def test_create_dynamic_array(self):
        arr = DynamicArray(5)
        self.assertEqual(arr.getCapacity(), 5)
        self.assertEqual(arr.getSize(), 0)

    def test_get_set_elements(self):
        arr = DynamicArray(3)
        arr.set(0, 10)
        arr.set(1, 20)
        arr.set(2, 30)
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 20)
        self.assertEqual(arr.get(2), 30)
        with self.assertRaises(IndexError):
            arr.get(3)
        with self.assertRaises(IndexError):
            arr.set(3, 40)

    def test_push_back(self):
        arr = DynamicArray(3)
        arr.pushback(10)
        arr.pushback(20)
        arr.pushback(30)
        self.assertEqual(arr.getSize(), 3)
        self.assertEqual(arr.getCapacity(), 3)
        arr.pushback(40)
        self.assertEqual(arr.getSize(), 4)
        self.assertEqual(arr.getCapacity(), 6)

    def test_pop_back(self):
        arr = DynamicArray(3)
        arr.pushback(10)
        arr.pushback(20)
        arr.pushback(30)
        self.assertEqual(arr.popback(), 30)
        self.assertEqual(arr.getSize(), 2)
        self.assertEqual(arr.getCapacity(), 3)
        with self.assertRaises(IndexError):
            arr.popback()
            arr.popback()
            arr.popback()

if __name__ == '__main__':
    unittest.main()