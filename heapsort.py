class Heap(object):
    def __init__(self, array):
        self._array = array
        self.size = len(array)
        self.heapify()

    def heapify(self):
        for i in range((self.size-1)//2, -1, -1):
            self.maintain_heap(i)

    def maintain_heap(self, root):
        left = root*2+1
        right = root*2+2
        max_node = root
        if left < self.size and self._array[left] > self._array[max_node]:
            max_node = left
        if right < self.size and self._array[right] > self._array[max_node]:
            max_node = right
        if max_node != root:
            max_val = self._array[max_node]
            self._array[max_node] = self._array[root]
            self._array[root] = max_val
            self.maintain_heap(max_node)

    def pop(self):
        root_val = self._array[0]
        self._array[0] = self._array[self.size-1]
        self._array[self.size-1] = root_val
        self.size -= 1
        self.maintain_heap(0)
        return root_val

    def is_not_empty(self):
        return self.size>0

if __name__ == '__main__':
    A = [5, 2, 1, 10, 13, 7, 8, 8, -1, 7]
    max_heap = Heap(A)
    while(max_heap.is_not_empty()):
        max_heap.pop()
    print max_heap._array