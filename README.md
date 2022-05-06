### Intro
This package allows finding the minimal element in a specific type of array. 
See [task description](#task-description) below for details.

### Environment
This package has been tested in:

`python` versions `3.6`, `3.7`, `3.8`, `3.9` and `3.10` 

OS: `Linux` and `Windows`

### Package installation and tests
To install, while activated in a virtualenv, issue:
```bash
pip install --upgrade pip git+https://github.com/noamba/minimum.git@0.2.2
```

Tests are included in the package, to run them issue:
```bash
python -m pytest -v --pyargs minimum
```

### Usage example
Activated in the virtualenv, issue:
```bash
python
```

In the python shell, issue:
```python
from minimum import get_minimum
get_minimum([5, 4, 3, 2, 3, 4])
```

### Development installation

Note: These instructions were tested on a `Linux` machine

```bash
git clone https://github.com/noamba/minimum.git
cd minimum
```

Create and activate a virtualenv, then issue:
```bash
make deps  # to install dependencies
make test
```

This will add a `htmlcov` folder with test coverage info. 
Open the `index.html` file within that folder in a browser to view the coverage report.

To run nox tests (requires `python` `3.8` and `3.9`), issue:
```bash
nox
```

To create an editable installation, issue:
```bash
pip install -e .
```



### Task description 

Please implement a Python module, which can be installed using pip**, including tests,
with the following functionality:

Given an array of elements that provide a less
than operator, find the minimum using as few comparisons as possible.

The array shall be given such that the first few elements are strictly monotonically
decreasing, the remaining elements are strictly monotonically increasing.

The less than operator be defined as the operator that works on such
vectors where a < b if min(a,b) == a.

** no need to upload it to pypi.org
