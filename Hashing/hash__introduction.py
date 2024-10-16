
# >>>>>__________<<<<<<<

# 1____best_case: O(1)
# 2____ Worst_case: O(n) if ON collision other's_ O(n)
# 3___Average_case: O(1+a) --->>>> a = (n/m) -->> N number's data and m number's index


# hash_table
# hash_size
# hash_Function

hash_size = 5


hash_table = [[] for  i in range(hash_size)]   # hashing__list

# create index in hash_table
def hash_function(data):
    return hash(data) % hash_size       # input_data % hash_size


def search_data(data):
    for i in range(hash_size):
        if hash_table[i] == [data]:
            return True
    return None

def remove(data):
    hash_table_index = hash_function(data)
    if hash_table[hash_table_index] == [data]:
        return hash_table.pop(hash_table_index)


# hash_table >>>> Add >> data
def insert_hashTable_data(data):
    hashTable_index_place = hash_function(data)
    hash_table[hashTable_index_place].append(data)

if __name__ == '__main__':

    insert_hashTable_data(10)   # data % size : 10%5 = 0

     # [[10],[],[],[],[]]  list
     #   0   1  2  3  4   index


    insert_hashTable_data(11)   # data % size : 10%5 = 1

    # [[],[11],[],[],[]]  list
    #   0   1  2  3  4   index

    insert_hashTable_data(13)   # data % size : 13%5 = 3

    #hash_list:  [[],[],[],[13],[]]
    # hash_index  0   1  2  3  4

    insert_hashTable_data(20)  # data % size : 20 % 5 = 0
    # [[10,20],[11],[],[],[]]  list
    #   0   1  2  3  4   index

    print("Hash_table: ",hash_table)

    print(search_data(13))  # Chack data

    print()


    print("Before removing hash_table: ", hash_table)
    # remove data in heap_list
    Re = remove(13)
    print(Re)

    print("After removing hash_table : ", hash_table)






















