#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
     # last element is the one with destination of NONE
    # first element is one which doean't appear as a destination
    sources = {}
    for ticket in tickets:
        sources[ticket.source] = ticket.destination
    # find first element
    route = []
    current = "NONE"
    for _ in range(len(tickets)):
        route.append(sources[current])
        current = sources[current]

    return route
