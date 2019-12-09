from __future__ import absolute_import  # No implicit relative imports
from __future__ import print_function
from __future__ import division
from builtins import range

from rain import function_two

GLOBAL_VARIABLE_THREE = 3


def function_three():
    return function_two(1)
