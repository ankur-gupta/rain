from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

from rain import Iterable

GLOBAL_VARIABLE_ONE = 1


def function_one(x=[1, 2, 3]):
    assert isinstance(x, Iterable)
    return 'one'
