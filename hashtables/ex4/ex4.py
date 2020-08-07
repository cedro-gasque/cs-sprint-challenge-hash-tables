from hashtable import HashTable

hash = HashTable(1024)
def has_negatives(a):
    hash = HashTable(1024)
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for n in a:
        pair = hash.get(str(- n))
        if pair:
            result.push(abs(pair))
        else:
            hash.put(str(n), True)
    return None



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
