import os

from rain.version import __version__
from rain.circular.array import Array
from rain.circular.grouped_array import GroupedArray

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_path(partial_path=''):
    return os.path.join(_ROOT, partial_path)


def load_mathematicians(partial_path='resources/mathematicians.txt'):
    path = get_path(partial_path)
    with open(path, 'r') as f:
        mathematicians = f.readlines()
    mathematicians = [m.strip() for m in mathematicians]
    return mathematicians
