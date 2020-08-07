from hashtable import HashTable

hash = HashTable(1024)
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    arrs = sorted(arrays, key=len)
    for arr in arrs:
        for i in arr:
            if 
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
