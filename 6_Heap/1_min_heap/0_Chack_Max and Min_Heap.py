



def is_Min_heap(H):
    n = len(H) - 1
    for i in range(n, 0, -1):
        p = parent(i)
        if p >= 1 and H[p] > H[i]:  # Make sure to check only valid parents
            return False
    return True




def left_child(i):
    return i * 2


def right_child(i):
    return i * 2 + 1


def parent(i):
    return i // 2


def is_max_heap(H):
    n = len(H) - 1
    for i in range(n, 0, -1):
        p = parent(i)
        if p >= 1 and H[p] < H[i]:  # Make sure to check only valid parents
            return False
    return True


if __name__ == '__main__':
    # Taking space-separated integer input to build the heap
    h = [None] + list(map(int, input("Enter heap elements (space-separated): ").split()))

    # Input for the node index
    index = int(input("Enter the index to check: "))

    # Calculate and print parent, left child, and right child of the node at 'index'
    if index < len(h):
        p = parent(index)
        l = left_child(index)
        r = right_child(index)

        print(f"Parent of node {index}: {p if p >= 1 else None}")
        print(f"Left child of node {index}: {l if l < len(h) else None}")
        print(f"Right child of node {index}: {r if r < len(h) else None}")
    else:
        print(f"Index {index} is out of range.")

    # Check if the given heap is a max-heap and print result
    if is_max_heap(h):
        print("The heap is a valid max-heap.")
    else:
        print("The heap is not a valid max-heap.")


    print("..........................................")



    if is_Min_heap(h):
        print("the heap is a valid min_heap")
    else:
        print("the heap is not a valid min_heap")


def is_min_heap(H):
    n = len(H)-1
    for i in range(n,0,-1):
        h = parent(i)
        if H[h] > H[i]:
            return False
        return True




if __name__ == '__main__':
    H  = [12,8,9,1,2]
    if is_max_heap(H):
        print("it is Max Heap")
    else:
        print("It is a not max heap")


    H = [2,3,4,10,20,30,40]

    if is_max_heap(H):
        print("is A min heap list")

    else:
        print("is't mean heap")



    print(left_child(H[1]))


