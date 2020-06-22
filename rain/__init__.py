import logging
import os

from rain.version import __version__
from rain.compat import Iterable
from rain.module_one import function_one
from rain.module_two import function_two
from rain.module_three import function_three, function_four

# The order of these imports illustrates an important point of using
# either explicit relative imports or absolute "full-path" import
# in $REPO_ROOT/rain/module_fruits.py file. In the next line, we import
# `banana()` from $REPO_ROOT/rain/module_fruits.py before we import
# `plantain()` from $REPO_ROOT/rain/module_plantain.py. But, `banana()`
# depends on `plantain()` which means that $REPO_ROOT/rain/module_fruits.py
# needs to make `plantain()` available without depending on this __init__.py
# file.
from rain.module_fruits import apple, banana
from rain.module_plantain import plantain

# Import from the files that demonstrates circular dependencies.
# If we comment out the two lines below, then we may not encounter any
# ImportError even if our circular imports are incorrect. This is because
# ImportError due to circular imports occurs only when we actually import
# from one of the files that are involved in the circular import. But the
# error would exist and would appear when the user tries to import Array
# or GroupedArray. Otherwise, these lines don't interfere with circular
# imports at all.
from rain.module_circular.array import Array
from rain.module_circular.group import GroupedArray

# Define a logger for the whole package
# See
# https://realpython.com/python-logging-source-code/#library-vs-application-logging-what-is-nullhandler
# https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
# https://stackoverflow.com/questions/27016870/how-should-logging-be-used-in-a-python-package
logging.getLogger(__name__).addHandler(logging.NullHandler())

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_path(partial_path=''):
    return os.path.join(_ROOT, partial_path)


def load_mathematicians(partial_path='resources/mathematicians.txt'):
    path = get_path(partial_path)
    with open(path, 'r') as f:
        mathematicians = f.readlines()
    mathematicians = [m.strip() for m in mathematicians]
    return mathematicians
