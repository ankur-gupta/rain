from __future__ import absolute_import  # No implicit relative imports
from __future__ import print_function
from __future__ import division
from builtins import range

import logging
from rain.module_one import function_one, GLOBAL_VARIABLE_ONE

GLOBAL_VARIABLE_TWO = 2

logger = logging.getLogger(__name__)


def function_two(x):
    y = GLOBAL_VARIABLE_ONE + GLOBAL_VARIABLE_TWO
    logger.info('Inside rain.module_two.function_two()')
    return function_one()
