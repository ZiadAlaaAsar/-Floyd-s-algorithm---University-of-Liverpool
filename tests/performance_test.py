import sys
import cProfile
from floydwarshall.floyd_warshall import floyd_recursive
from floyd_warshall_iterative import floyd

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

# Performance test on the recursive version
print("cProfile results of the recursive version: ")
cProfile.run("floyd_recursive(graph)")
# Performance test on the iterative version
print("cProfile results of the iterative version: ")
cProfile.run("floyd(graph)")
