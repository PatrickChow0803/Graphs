from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            raise Exception('Vertex not found')
        self.vertices[v1] = {*self.vertices[v1], v2}

    def bfs_furthest_vertex(self, starting_vertex):
        """
        Returns the vertex furthest from the starting vertex
        If there is more than one vertex tied for furthest, return the one with the lowest numeric ID.
        """

        q = Queue()
        path = []
        greatest_distance = [0,0]
        visited = set()
        q.enqueue([starting_vertex])
        # while the queue isn't empty
        while q.size() > 0:
            path = q.dequeue()
            # If the node hasn't been visited yet
            if path[-1] not in visited:
                # Enqueue each neighbor vertex to the queue.
                for edge in self.vertices[path[-1]]:
                    q.enqueue(list([*path, edge]))
                    # Add each of the neighbor to the visited set.
                    visited.add(path[-1])
                # If the vertex is equal to the set, set greatest_distance[1] equal to path[-1]
                if self.vertices[path[-1]] == set():
                    if len(path) ==  greatest_distance[0]:
                        # Used to return the lowest value node on a tie
                        if path[-1] < greatest_distance[1]:
                            greatest_distance[1] = path[-1]
                    if len(path) > greatest_distance[0]:
                        greatest_distance[0] = len(path)
                        greatest_distance[1] = path[-1]
        # greatest_distance[1] is the vertex furthest away from the starting vertex.
        return greatest_distance[1]
