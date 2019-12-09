from __future__ import absolute_import  # No implicit relative imports
from __future__ import print_function
from __future__ import division
from builtins import range

# This file illustrates that when using absolute imports, using the full path
# to the module is important. The function `banana()` depends on `plantain()`
# which is defined in $REPO_ROOT/rain/module_plantain.py. We cannot depend on
# $REPO_ROOT/rain/__init__.py file to provide the `plantain()` to this file.
# In other words, the following line in this file would've failed
# because of the order of imports in $REPO_ROOT/rain/__init__.py file:
#     from rain import plantain  # fails!
# But, an explicit relative import would work:
#     from .module_plantain import plantain  # works!
# Note: PyCharm, by default, adds absolute "full-path" imports.
# Absolute "full-path" imports are the recommended way to import within a
# package though explicit relative imports are okay. Implicit relative imports
# are not allowed in Python 3 and are disabled by importing `absolute_import`
# from `__future__`.
# See https://stackoverflow.com/questions/5811463/when-to-use-absolute-imports
from rain.module_plantain import plantain


def banana():
    return plantain()


def apple():
    return 'apple'
