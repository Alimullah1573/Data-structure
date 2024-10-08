


def left_child(i):
    return i*2

def right_child(i):
    i*2+1

def parent(i):
    return i//2

def is_max_heap(H):
    n = len(H)-1

    for i in range(n,1,-1):
        p = parent(i)
        if H[p] < H[i]:
            return False

        return True

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


