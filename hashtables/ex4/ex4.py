def has_negatives(a):
    hash = dict()
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for n in a:
        if n in hash:
            v = max(n, hash[n])
            if not v in result:
                result.append(max(n, hash[n]))
        else:
            hash[-n] = n
    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
