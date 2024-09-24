# Dynamic Array implementation
# Design Dynamic Array (Resizable Array)
# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Your DynamicArray class should support the following operations:

# DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
# int get(int i) will return the element at index i. Assume that index i is valid.
# void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
# void pushback(int n) will push the element n to the end of the array.
# int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
# void resize() will double the capacity of the array.
# int getSize() will return the number of elements in the array.
# int getCapacity() will return the capacity of the array.
# If we call void pushback(int n) but the array is full, we should resize the array first.

# Example 1:
# Input:
# ["Array", 1, "getSize", "getCapacity"]

# Output:
# [null, 0, 1]

# Example 2:
# Input:
# ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

# Output:
# [null, null, 1, null, 2]

# Example 3:
# Input:
# ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
# Output:
# [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
# Note:
# The index i provided to get(int i) and set(int i) is guaranteed to be greater than or equal to 0 and less than the number of elements in the array.

# Note: Python lists are dynamic arrays by default,
# but this is an example of what's going on under the hood.

class DynamicArray:
    def __init__(self, capacity=1):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of range")
        return self.arr[i]

    def set(self, i, n):
        if i < 0 or i >= self.capacity:
            raise IndexError("Index out of range")
        self.arr[i] = n
        # Adjust size if setting an index larger than current size
        if i >= self.size:
            self.size = i + 1

    def pushback(self, n):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self):
        if self.size == 0:
            raise IndexError("Array is empty")
        self.size -= 1
        return self.arr[self.size]

    def resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity