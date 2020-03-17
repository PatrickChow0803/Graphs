import os
import sys
sys.path.append("../graph")
from graph import Graph

from graph import Graph

# Find the node furthest away from the starting_node that's connected.
# If there's multiple ancestor, take the ancestor with the lower integer
def earliest_ancestor(ancestors, starting_node):
    # Create the graph that will hold the vertices and edges
    graph = Graph()
    for ancestor in ancestors:
        # Adds the first and second vertex
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        # Connects the vertex
        graph.add_edge(ancestor[1], ancestor[0])

    solution = graph.bfs_furthest_vertex(starting_node)
    if starting_node == solution:
        return -1
    else:
        return solution
