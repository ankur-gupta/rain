from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

from rain import function_one
from .module_one import GLOBAL_VARIABLE_ONE

GLOBAL_VARIABLE_TWO = 2


def function_two(x):
    y = GLOBAL_VARIABLE_ONE + GLOBAL_VARIABLE_TWO
    return function_one()
