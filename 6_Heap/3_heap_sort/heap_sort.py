
#    1__>>>   Insert: O(log n)
#    2__>>>   Heapify u p /down: O(log n)
#    3__>>>   Build max heap: O(n)
#    4__>>>   Heap sort: O(n log n)
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        # Return the index of the parent of the current node
        return (i - 1) // 2

    def _heapify_up(self, i):
        # Ensure the heap property is maintained from the inserted node up to the root
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            # Swap if the parent is smaller than the current node
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def insert(self, value):
        # Insert a new value into the heap and restore the heap property by heapifying up
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_down(self, i, heap_size):
        # Maintain the heap property from the root down to the leaves
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # Check if left child exists and is greater than the current largest
        if left_child < heap_size and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        # Check if right child exists and is greater than the current largest
        if right_child < heap_size and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        # If the largest is not the current node, swap and continue heapifying down
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest, heap_size)

    def build_max_heap(self):
        # Convert the array into a max-heap by heapifying down from the last non-leaf node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i, len(self.heap))

    def heap_sort(self):
        # First, build a max-heap from the current heap
        self.build_max_heap()

        # Initialize the heap size
        heap_size = len(self.heap)

        # Swap the first element (largest) with the last element and reduce heap size
        for i in range(len(self.heap) - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            heap_size -= 1  # Reduce the size of the heap
            self._heapify_down(0, heap_size)  # Restore the heap property for the reduced heap

        return self.heap  # The array is now sorted in ascending order


# Example
if __name__ == '__main__':
    heap_sorter = MaxHeap()
    values = [100, 50, 30, 21, 1]

    # Insert values to build the heap
    for value in values:
        heap_sorter.insert(value)

    print("Unsorted heap:", heap_sorter.heap)

    # Perform heap sort
    sorted_values = heap_sorter.heap_sort()
    print("Sorted values:", sorted_values)
