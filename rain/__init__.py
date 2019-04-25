import os

from .version import __version__
from .compat import Iterable
from .module_one import function_one
from .module_two import function_two
from .module_three import function_three, function_four

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_path(partial_path=''):
    return os.path.join(_ROOT, partial_path)


def load_mathematicians(partial_path='resources/mathematicians.txt'):
    path = get_path(partial_path)
    with open(path, 'r') as f:
        mathematicians = f.readlines()
    mathematicians = [m.strip() for m in mathematicians]
    return mathematicians
