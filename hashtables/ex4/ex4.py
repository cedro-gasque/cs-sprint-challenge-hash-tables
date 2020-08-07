from hashtable import HashTable

hash = HashTable(1024)
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for n in a:
        if hash.get(-n):
            result.append(n)
        else:
            hash.put(n, -n)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
