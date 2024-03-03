# Floyd-Warshall Algorithm (LIVMidMod_Assignment)

The Floyd-Waarshall algorithm (also known as the WFI algorithm) is an algorithm for finding the shortest paths between all of the points of a graph.
Also, this graph can be a weighted graph with positive or negative vertices (but with no negative cycles).

This is a Python package to use the Floyd-Warshall algorithm to calculate the distance matrix in an adjacency matrix.

This package uses a recursive version of the algorithm, re-written from the iterative version in the root folder of this package.

This package is written using PEP 8 guidelines.

How Floyd's algorithm work?

First of all you need a graph like Below:

![image](https://github.com/ZiadAlaaAsar/-Floyd-s-algorithm---University-of-Liverpool/assets/86348020/752d407e-20aa-41cc-8c00-516261e51b29)

Then we should make a matrix of paths (i is the start point and j is the finish point); if i equals j, we put 0, if the start point and end point don't have neighbors, we put infinite, and if two points are neighbors, we put the degree of the start point. Look at the below matrix

![image](https://github.com/ZiadAlaaAsar/-Floyd-s-algorithm---University-of-Liverpool/assets/86348020/1c2ea6c9-c9fa-4ad5-9796-928265a1f6d8)

And then we have to change the values to the shortest paths.


## Table of Contents

- [Install](#Install)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)

## Install

This package is written using `Python 3.11.7`.

To install this package use pip:
```sh
pip install git+https://github.com/ZiadAlaaAsar/-Floyd-s-algorithm---University-of-Liverpool
```

To install the dependencies use pip:
```sh
pip install -r requirements.txt
```

## Usage

To use this package, you could import it into your script:
```sh
from floydwarshall.floyd_warshall import floyd_recursive
```

Alternatively, you could run it from your IDE or CLI as below (from the repository's root directory):
```sh
python floydwarshall/floyd_warshall.py
```

The script accepts data in the form of a graph square matrix in the following format:

`graph = [[0, 7, NO_PATH, 8],[NO_PATH, 0, 5, NO_PATH],[NO_PATH, NO_PATH, 0, 2],[NO_PATH, NO_PATH, NO_PATH, 0]]`

Where there is no path between nodes or it is unknown, this is set as below:
```sh
import sys
NO_PATH = sys.maxsize
```

### Performance Tests

Performance tests are run using `cProfile`. 

To run the performance tests, run the below command:
```sh
python tests/performance_test.py
```

### Unit Tests

Unit tests are run using `unittest`. 

To run the unit tests, run the below command:
```sh
python -m unittest
```

## Contributing

Please open a PR for contributions.

## License

MIT License.

See license in [LICENSE](floyd-warshall-algorithm/LICENSE)
