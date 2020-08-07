#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtable import HashTable

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = HashTable(1024)
    for ticket in tickets:
        hash.put(ticket.source, ticket.destination)
    route = list()
    s = hash.get("NONE")
    while not s is "NONE":
        route.append(s)
        s = hash.get(s)
    route.append(s)
    return route
