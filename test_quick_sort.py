from unittest import TestCase
from quicksort import quick_sort, quick_sort_classic, quick_sort_original
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
        import time
        N = 10000
        random.seed(0)
        A = []
        for i in range(N):
            A.append(int(random.random()*N*10))
        A_copy = list(A)
        t0 = time.time()
        quick_sort(A)
        t1 = time.time()
        A_sorted = sorted(A_copy)
        t2 = time.time()
        print "My algo takes %f s vs native %f s with ratio %f" %(t1-t0, t2-t1, (t1-t0)/(t2-t1))
        self.assert_list_equal(A, A_sorted)

    def test_quick_sort_classic(self):
        import time
        N = 10000
        random.seed(0)
        A = []
        for i in range(N):
            A.append(int(random.random()*N*10))
        A_copy = list(A)
        t0 = time.time()
        quick_sort_classic(A)
        t1 = time.time()
        A_sorted = sorted(A_copy)
        t2 = time.time()
        print "Classic algo takes %f s vs native %f s with ratio %f" %(t1-t0, t2-t1, (t1-t0)/(t2-t1))
        self.assert_list_equal(A, A_sorted)

    def test_quick_sort_orignal(self):
        import time
        N = 10000
        random.seed(0)
        A = []
        for i in range(N):
            A.append(int(random.random()*N*10))
        A_copy = list(A)
        t0 = time.time()
        quick_sort_original(A)
        t1 = time.time()
        A_sorted = sorted(A_copy)
        t2 = time.time()
        print "Original algo takes %f s vs native %f s with ratio %f" %(t1-t0, t2-t1, (t1-t0)/(t2-t1))
        self.assert_list_equal(A, A_sorted)