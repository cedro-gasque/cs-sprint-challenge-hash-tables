# Your code here
from hashtable import HashTable

def finder(files, queries):
    hash = HashTable(2 ** 21)
    """
    YOUR CODE HERE
    """
    # Your code here

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
