""" Floyd-Warshall Algorithm

This script calculates the shortest distance between nodes in an adjacency matrix using
Floyd-Warshal algorithm in recursion.

The script accepts data in the form of a graph square matrix in the following format:
[[0, 7, NO_PATH, 8],[NO_PATH, 0, 5, NO_PATH]]
"""

import sys
from functools import lru_cache

# Set NO_PATH value for when there is no path between the start and end nodes.
NO_PATH = sys.maxsize
# Sample graph square matrix (nxn).
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]


def floyd_recursive(distance):
    """Returns the updated graph matrix after calculating the shortest distance.

    Argument:
    distance - the distance matrix.
    """
    # Find the number of nodes in the graph matrix.
    max_length = len(distance[0])

    # Caches the results of the function to improve the recursion performance.
    @lru_cache(maxsize=None)
    def shortest_distance(i, j, k):
        """Returns the shortest distance between nodes i and j using recursion.

        Arguments:
        i -- the start node
        j -- the end node
        k -- the intermediary node
        """
        # Recursion base case to stop the recursion.
        if k < 0:
            return distance[i][j]

        # Recursive case to find the shortest distance.
        return min(shortest_distance(i, j, k-1),
                   shortest_distance(i, k, k-1) +
                   shortest_distance(k, j, k-1))

    # Loop through the nodes in the graph matrix.
    for k in range(max_length):
        for i in range(max_length):
            for j in range(max_length):
                # If the start node and end node are the same
                # then the distance will be 0.
                if i == j:
                    distance[i][j] = 0
                    continue
                # Call the nested function to calculate the shortest distance.
                distance[i][j] = shortest_distance(i, j, k)
    return distance


if __name__ == '__main__':
    # Call the function and pass the graph matrix.
    updated_matrix = floyd_recursive(graph)
    print(updated_matrix)
