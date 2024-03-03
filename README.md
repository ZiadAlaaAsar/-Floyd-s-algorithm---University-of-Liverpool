# Floyd-Warshall Recursive Algorithm (LIVMidMod_AssignmentCode)

This is a Python package to use the Floyd-Warshall algorithm to calculate the distance matrix in an adjacency matrix.

This package uses a recursive version of the algorithm, re-written from the iterative version in the root folder of this package.

This package is written using PEP 8 guidelines.

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
