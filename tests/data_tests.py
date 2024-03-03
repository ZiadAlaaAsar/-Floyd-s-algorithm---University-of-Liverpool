import sys

# Test data to be used in the /tests directory

NO_PATH = sys.maxsize

# Original graph matrix (4x4)
original_graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

original_expected = [
    [0, 7, 12, 8],
    [NO_PATH, 0, 5, 7],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

# Test cases
# test_a - 5x5 adjacency matrix
test_a = [
    [0, 4, 2, 5, NO_PATH],
    [1, 0, NO_PATH, 7, 3],
    [NO_PATH, 5, 0, 2, 4],
    [2, 6, 4, 0, 7],
    [3, 1, NO_PATH, 5, 0]
]

a_expected = [
    [0, 4, 2, 4, 6],
    [1, 0, 3, 5, 3],
    [4, 5, 0, 2, 4],
    [2, 6, 4, 0, 7],
    [2, 1, 4, 5, 0]
]

# test_b - 8x8 adjacency matrix
test_b = [
    [0, NO_PATH, 2, 1, 3, NO_PATH, 5, 7],
    [1, 0, 8, 7, NO_PATH, 3, 4, 2],
    [NO_PATH, NO_PATH, 0, 2, 4, 1, 5, 6],
    [2, 6, 4, 0, 7, NO_PATH, NO_PATH, 3],
    [3, 1, NO_PATH, 5, 0, 4, 2, NO_PATH],
    [5, 7, NO_PATH, 4, 2, 0, 1, 5],
    [1, NO_PATH, 8, NO_PATH, 3, 4, 0, 6],
    [6, NO_PATH, 2, 1, NO_PATH, 7, 1, 0]
]

b_expected = [
    [0, 4, 2, 1, 3, 3, 4, 4],
    [1, 0, 3, 2, 4, 3, 3, 2],
    [3, 4, 0, 2, 3, 1, 2, 5],
    [2, 6, 4, 0, 5, 5, 4, 3],
    [2, 1, 4, 3, 0, 4, 2, 3],
    [2, 3, 4, 3, 2, 0, 1, 5],
    [1, 4, 3, 2, 3, 4, 0, 5],
    [2, 5, 2, 1, 4, 3, 1, 0]
]

# test_c - float values
test_c = [
    [0, 4.2, 2, 5, NO_PATH],
    [1, 0, NO_PATH, 7, 3.5],
    [NO_PATH, 5.77, 0, 2, 4],
    [2, 6.12, 4, 0, 7],
    [3, 1.1, NO_PATH, 5, 0]
]

c_expected = [
    [0, 4.2, 2, 4, 6],
    [1, 0, 3, 5, 3.5],
    [4, 5.1, 0, 2, 4],
    [2, 6.12, 4, 0, 7],
    [2.1, 1.1, 4.1, 5, 0]
]

# test_d - non-square adjacency matrix, expected error
test_d = [
    [0, 4, 2, 5, NO_PATH],
    [1, 0, NO_PATH, 7, 3],
    [NO_PATH, 5],
    [2, 6, 4, 0, 7],
    [3, 1, NO_PATH, 5]
]

# test_e - 16x16 adjacency matrix
test_e = [
    [0, NO_PATH, 2, 1, 3, NO_PATH, 5, 7, 4, NO_PATH, 6, 1, NO_PATH, NO_PATH, 5, 3],
    [1, 0, 8, 7, NO_PATH, 3, 4, 2, 5, 4, NO_PATH, NO_PATH, 7, 3, 2, 1],
    [NO_PATH, NO_PATH, 0, 2, 4, 1, 5, 6, NO_PATH, NO_PATH, 1, NO_PATH, 2, 4, 7, 3],
    [2, 6, 4, 0, 7, NO_PATH, NO_PATH, 3, 1, 2, 5, 6, 3, 4, 6, 8],
    [3, 1, NO_PATH, 5, 0, 4, 2, NO_PATH, 6, 2, NO_PATH, 1, NO_PATH, 5, 7, NO_PATH],
    [5, 7, NO_PATH, 4, 2, 0, 1, 5, 3, 1, NO_PATH, 4, 1, NO_PATH, NO_PATH, 7],
    [1, NO_PATH, 8, NO_PATH, 3, 4, 0, 6, 1, NO_PATH, 5, 2, NO_PATH, 7, 2, 3],
    [6, NO_PATH, 2, 1, NO_PATH, 7, 1, 0, NO_PATH, 2, 3, 5, 8, 1, 3, 2],
    [4, NO_PATH, 2, 1, 3, NO_PATH, 5, 7, 0, 3, 2, 5, NO_PATH, NO_PATH, 1, 5],
    [1, NO_PATH, 7, 7, NO_PATH, 3, 4, 2, NO_PATH, 0, 1, 4, 6, NO_PATH, 2, 3],
    [NO_PATH, 4, NO_PATH, 2, 4, NO_PATH, 5, 6, 1, 3, 0, 2, 2, 8, NO_PATH, NO_PATH],
    [2, 6, 4, NO_PATH, 7, NO_PATH, NO_PATH, 3, 1, 1, 3, 0, 4, NO_PATH, 4, 2],
    [3, 2, NO_PATH, 5, NO_PATH, 4, 2, NO_PATH, 5, 7, 2, 2, 0, 4, 5, NO_PATH],
    [4, 7, NO_PATH, 4, 2, NO_PATH, 1, 5, 1, 2, 1, 2, 4, 0, 6, 3],
    [1, NO_PATH, 5, NO_PATH, 3, 4, NO_PATH, 3, 3, 1, 5, 7, 2, 4, 0, 7],
    [6, NO_PATH, 2, 2, NO_PATH, 3, 1, NO_PATH, 5, 7, 2, NO_PATH, NO_PATH, 3, 5, 0]
]

e_expected = [
    [0, 4, 2, 1, 3, 3, 4, 4, 2, 2, 3, 1, 4, 5, 3, 3],
    [1, 0, 3, 2, 4, 3, 2, 2, 3, 3, 3, 2, 4, 3, 2, 1],
    [3, 4, 0, 2, 3, 1, 2, 4, 2, 2, 1, 3, 2, 4, 3, 3],
    [2, 5, 3, 0, 4, 4, 4, 3, 1, 2, 3, 3, 3, 4, 2, 5],
    [2, 1, 4, 3, 0, 4, 2, 3, 2, 2, 3, 1, 5, 4, 3, 2],
    [2, 3, 4, 3, 2, 0, 1, 3, 2, 1, 2, 3, 1, 4, 3, 4],
    [1, 4, 3, 2, 3, 4, 0, 5, 1, 3, 3, 2, 4, 6, 2, 3],
    [2, 4, 2, 1, 3, 3, 1, 0, 2, 2, 2, 3, 4, 1, 3, 2],
    [2, 4, 2, 1, 3, 3, 4, 4, 0, 2, 2, 3, 3, 5, 1, 5],
    [1, 5, 3, 2, 4, 3, 3, 2, 2, 0, 1, 2, 3, 3, 2, 3],
    [3, 4, 3, 2, 4, 4, 4, 5, 1, 3, 0, 2, 2, 6, 2, 4],
    [2, 5, 3, 2, 4, 4, 3, 3, 1, 1, 2, 0, 4, 4, 2, 2],
    [3, 2, 5, 4, 5, 4, 2, 4, 3, 3, 2, 2, 0, 4, 4, 3],
    [2, 3, 3, 2, 2, 4, 1, 4, 1, 2, 1, 2, 3, 0, 2, 3],
    [1, 4, 3, 2, 3, 4, 4, 3, 3, 1, 2, 2, 2, 4, 0, 4],
    [2, 5, 2, 2, 4, 3, 1, 5, 2, 4, 2, 3, 4, 3, 3, 0]
]
