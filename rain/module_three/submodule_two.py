from __future__ import absolute_import  # No implicit relative imports
from __future__ import print_function
from __future__ import division
from builtins import range

import logging

GLOBAL_VARIABLE_FOUR = 4

logger = logging.getLogger(__name__)


def function_four():
    logger.info('In rain.module_three.submodule_two.function_four()')
    return 'four'
