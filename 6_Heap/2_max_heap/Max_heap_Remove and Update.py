class MinHeap:
    def __init__(self):
        self.heap = []  # Stores heap values

    def parent(self, i):
        return (i - 1) // 2

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap with parent
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def insert(self, value):
        self.heap.append(value)  # Add value to heap
        self._heapify_up(len(self.heap) - 1)  # Restore heap property

    def _heapify_down(self, i):
        smallest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            # Swap with the smallest child and continue heapifying down
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def remove(self, i):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        removed_value = self.heap[i]
        self.heap[i] = self.heap.pop()  # Replace with the last element
        self._heapify_down(i)  # Restore heap property from index i
        return removed_value


if __name__ == '__main__':
    min_heap = MinHeap()

    # Inserting values into the min heap
    min_heap.insert(100)
    min_heap.insert(50)
    min_heap.insert(30)
    min_heap.insert(21)
    min_heap.insert(1)

    # Heap before removal
    print("Heap before removal:", min_heap.heap)

    # Removing element at index 1
    removed = min_heap.remove(1)
    print("Removed element:", removed)

    # Heap after removal
    print("Heap after removal:", min_heap.heap)
