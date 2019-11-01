#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    print("::::::::::::::::::::::::::::")
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # source[0] = tickets[0].source
    for ticket in tickets:
        # print(ticket.source, ticket.destination)
        hash_table_insert(hashtable, ticket.destination, ticket.source)
        if ticket.destination is "NONE":
            route[length-1] = ticket.source
    print("r1", route)

    for i in range(length-1, 0, -1):
        prev_flight = hash_table_retrieve(hashtable, route[i])
        # print(tickets[i].source, prev_flight)
        route[i-1] = prev_flight
    route = route[1:]
    route.append("NONE")
    print("r2", route)
        

    return route
