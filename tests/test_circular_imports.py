import pytest

# If this import succeeds, then we successfully solved the circular import problem.
from rain import Array, GroupedArray


def test_basic():
    a = Array(range(3))
    assert a[0] == 0
    assert a[1] == 1
    assert a[2] == 2


def test_array_group():
    array = Array('aaaaabbbbcccdde')
    grouping = array.group()
    assert isinstance(grouping, GroupedArray)
    elements = {e for e in grouping.groups()}
    assert elements == {'a', 'b', 'c', 'd', 'e'}