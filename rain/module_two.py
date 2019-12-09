from __future__ import absolute_import  # No implicit relative imports
from __future__ import print_function
from __future__ import division
from builtins import range

from rain.module_one import function_one, GLOBAL_VARIABLE_ONE

GLOBAL_VARIABLE_TWO = 2


def function_two(x):
    y = GLOBAL_VARIABLE_ONE + GLOBAL_VARIABLE_TWO
    return function_one()
