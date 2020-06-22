from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

# This file should either be run from $REPO_ROOT (if rain is not installed)
# or anywhere (if rain is installed).

# Circular Imports
# rain.module_circular.Array and rain.module_circular.GroupedArray form
# a pair of circular imports:
# (1) Array.group() calls GroupedArray
# (2) GroupedArray.groups() calls Array
#
# Thus, we need to import GroupedArray in the file
# $REPO_ROOT/rain/module_circular/array.py and we need to import Array in the
# file $REPO_ROOT/rain/module_circular/group.py. If we write import
# statements at the beginning of both of these files (before Array or
# GroupedArray) are defined, then we will get an import error of the type
#
# ImportError: cannot import name 'Array' from 'rain.module_circular.array'
#
# We have solved it by importing Array locally. See README.md for more details
# on how to solve this issue in other ways. This file provides a demo of
# how to import circular dependencies without error


from rain import Array

x = Array([1, 2, 3, 1])
print(x)
print(x.group())
print(x.group().groups())
