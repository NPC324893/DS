
class Node:
    def __init__(self, key):
        self.key = key

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key


class UnsortedArray:
    def __init__(self):
        self.array = []
        self.size = 0

    def search(self, key):
        # O(n) time complexity
        for i in self.array:
            if i.get_key() == key:
                return True

        return False

    def insert(self, key):
        # O(1) time complexity
        new_node = Node(key)
        self.array.append(new_node)

    def remove(self, key):
        # O(n) time complexity
        for i in self.array:
            if i.get_key() == key:
                self.size -= 1
                self.array.remove(i)
                return True

        return False

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = []
            right = []
            for i in range(1, len(arr)):
                if arr[i] < pivot:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
            return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def find_median(self):
        # O(1) time complexity
        # first check if the array is empty
        if self.size == 0:
            return print('Array is Empty')

        # THEN check if there is only one key
        if self.size == 1:
            return print('Array Median is:', self.array[0].get_key() )

        sorted_array = self.quick_sort(self.array)

        # more than 1 key:
        if self.size % 2 != 0:
            # array has middle element
            return print('Array Median is:', sorted_array[self.size//2].get_key() )
        else:
            # need to get the average of the two middle elements
            # if array = [1,2] --> average will be 1.5
            first_middle = sorted_array[ (self.size//2)-1 ]
            second_middle = sorted_array[ self.size//2 ]
            average = (first_middle.get_key() + second_middle.get_key() )/2
            return print('Array Median is:', average)

