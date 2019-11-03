#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(0, len(weights)):
        print(i, weights[i])
        hash_table_insert(ht, weights[i], i)
    for item in weights:
        diff = limit - item
        other_index = hash_table_retrieve(ht, diff)
        if other_index != None:
            print("ind", diff, other_index)
            if other_index >= weights.index(item):
                print((other_index, weights.index(item)))
                return (other_index, weights.index(item))
            else:
                print((weights.index(item), other_index))
                return (weights.index(item), other_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
