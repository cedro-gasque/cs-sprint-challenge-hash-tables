from hashtable import HashTable

def get_indices_of_item_weights(weights, length, limit):
    hash = HashTable(1024)
    """
    YOUR CODE HERE
    """
    # Your code here
    for i, weight in enumerate(weights):
        pair = hash.get(str(limit - weight))
        if not pair is None:
            return sorted([pair, i], reverse=True)
        else:
            hash.put(str(weight), i)
    return None
