from unittest import TestCase
from heapsort import Heap, Node
import time


class TestHeap(TestCase):
    def verify_heap(self, max_heap):
        for i in range(max_heap.size//2):
            left = 2*i + 1
            right = 2*i + 2
            self.assertGreaterEqual(max_heap._array[i], max_heap._array[left])
            if right < max_heap.size:
                self.assertGreaterEqual(max_heap._array[i], max_heap._array[right])

    def test_create_heap(self):
        A = [5, 2, 1, 10, 13, 7, 8, 8, -1, 7]
        A = [Node({'key': i, 'val': time.ctime()}) for i in A]
        max_heap = Heap(A)
        self.verify_heap(max_heap)

    def test_insert(self):
        A = [5, 2, 1, 10, 13, 7, 8, 8, -1, 7]
        A = [Node({'key': i, 'val': time.ctime()}) for i in A]
        max_heap = Heap(A)
        max_heap.insert(Node({'key': 6, 'val': ''}))
        max_heap.insert(Node({'key': 18, 'val': ''}))
        max_heap.insert(Node({'key': 18, 'val': ''}))
        self.verify_heap(max_heap)

    def test_modify_key(self):
        A = [5, 2, 1, 10, 13, 7, 8, 8, -1, 7]
        A = [Node({'key': i, 'val': time.ctime()}) for i in A]
        max_heap = Heap(A)
        max_heap.modify_key(2, 5)
        max_heap.modify_key(18, 3)
        max_heap.modify_key(0, 2)
        self.verify_heap(max_heap)

    def test_pop(self):
        A = [5, 2, 1, 10, 13, 7, 8, 8, -1, 7]
        A = [Node({'key': i, 'val': time.ctime()}) for i in A]
        max_heap = Heap(A)
        self.assertEqual(max_heap.pop().key, 13)
        self.assertEqual(max_heap.pop().key, 10)
        self.verify_heap(max_heap)