from unittest import TestCase
from quicksort import quick_sort
import random

class TestQuick_sort(TestCase):
    def assert_list_equal(self, list_a, list_b):
        for i, j in zip(list_a, list_b):
            self.assertEqual(i, j)

    def test_quick_sort_1(self):
        A = [11, 1, 2, 5, 4, 3, 6, 13, 0, 2, 3, 6, 7, 15, 3]
        quick_sort(A)
        self.assert_list_equal(A,
            [0, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 11, 13, 15])

    def test_quick_sort_2(self):
        N = 1000
        random.seed(0)
        A = []
        for i in range(N):
            A.append(int(random.random()*10000))
        A_copy = list(A)
        quick_sort(A)
        self.assert_list_equal(A, sorted(A_copy))