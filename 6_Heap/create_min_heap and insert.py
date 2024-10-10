class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap with the parent
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def display(self):  # All heap View
        print(self.heap)


# Example usage:
if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    max_heap.insert(30)
    max_heap.insert(15)
    max_heap.insert(100)
    max_heap.insert(1)

    print("Max Heap:", max_heap.heap)

    max_heap.display()  # Max Heap View

    print("heap size :",max_heap.size())

    print(max_heap.heap[(max_heap.left_child(0))])       # chack left_child
    print(max_heap.heap[(max_heap.right_child(0))])     # chack right_child
    print(max_heap.heap[(max_heap.parent(1))])   # Chack Parent
    print(max_heap.heap[(max_heap.parent(2))]) # Chack Parent


