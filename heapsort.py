class Node(object):

    def __init__(self, prop_map):
        self.key = prop_map['key']
        del prop_map['key']
        self.val = prop_map

    def __repr__(self):
        return str(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key

    def __gt__(self, other):
        return self.key > other.key

    def __lt__(self, other):
        return self.key < other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __le__(self, other):
        return self.key <= other.key


class Heap(object):
    def __init__(self, array):
        self._array = array
        self.size = len(array)
        self.heapify(0)

    def heapify(self, root):
        for i in range((self.size-1)//2, root-1, -1):
            self.maintain_heap(i)

    def insert(self, node):
        if len(self._array) == self.size:
            self._array.append(node)
        else:
            self._array[self.size] = node
        self.size +=1
        self._increase_key(node.key, self.size-1)

    def modify_key(self, new_key, pos):
        if new_key > self._array[pos].key:
            self._increase_key(new_key, pos)
        elif new_key < self._array[pos].key:
            self._decrease_key(new_key, pos)

    def _increase_key(self, new_key, pos):
        self._array[pos].key = new_key
        parent = (pos-1)//2
        while parent >= 0 and self._array[pos] > self._array[parent]:
            parent_node = self._array[parent]
            self._array[parent] = self._array[pos]
            self._array[pos] = parent_node
            pos = parent
            parent = (pos-1)//2

    def _decrease_key(self, new_key, pos):
        self._array[pos].key = new_key
        self.maintain_heap(pos)

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

    def peek(self):
        return self._array[0]

    def is_not_empty(self):
        return self.size > 0

if __name__ == '__main__':
    import time
    import copy
    A = [5, 2, 1, 10, 13, 7, 8, 8, -1, 7]
    A = [Node({'key': i, 'val': time.ctime()}) for i in A]
    A_orgi = copy.deepcopy(A)
    max_heap = Heap(A)
    while(max_heap.is_not_empty()):
        max_heap.pop()
    print max_heap._array