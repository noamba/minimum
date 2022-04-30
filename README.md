### Intro
This package allows finding the minimal element in a specific type of array. 
See Task description for details. 

### Installation

```bash
pip install --upgrade pip git+https://github.com/noamba/minimum.git
```

### Usage example

In a virtualenv, issue:
```bash
python3
```

In the python shell, issue:
```python
from minimum import get_minimum
get_minimum([5, 4, 3, 2, 3, 4])
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
