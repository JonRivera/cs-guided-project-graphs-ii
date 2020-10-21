class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = LinkedListNode(item)
        # check if queue is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            # add new node to rear
            self.rear.next = new_node
            # reassign rear to new node
            self.rear = new_node

    def dequeue(self):
        # check if queue is empty
        if self.front is not None:
            # keep copy of old front
            old_front = self.front
            # set new front
            self.front = old_front.next

        # check if the queue is now empty
        if self.front is None:
            # make sure rear is also None
            self.rear = None

        return old_front


class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

    def add_connection(self, vert, weight=0):
        self.connections[vert] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, vert):
        return self.connections[vert]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def add_edge(self, v1, v2, weight=0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def breadth_first_search(self, starting_vert):
        to_visit = Queue()
        visited = set()
        to_visit.enqueue(starting_vert)
        visited.add(starting_vert)
        while to_visit.size() > 0:
            current_vert = to_visit.dequeue()  # this helps us perform a breadth search
            for next_vert in current_vert.get_connections():  # visiting the neighbors of the current vertix
                if next_vert not in visited:  # Every neighboor is being represented as a next_vertix
                    visited.add(next_vert) # so lonh as this vertix (aka the neighboor of current vertix) hasn't already been visiting continue
                    to_visit.enqueue(next_vert # enque it so that we can search the neightboors for next_ver in the the next layer(next depth)