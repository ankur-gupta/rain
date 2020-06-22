from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

# Neither the "absolute full-path" import nor the "explicit relative import"
# works. Both of these at the top of the script (before GroupedArray) is
# defined fails because of circular imports.
# Pandas solves this issue the same way. See this line:
# https://github.com/pandas-dev/pandas/blob/80ba4c4294a1ce1d95aeeb8e5de86d33ebb6edf4/pandas/core/groupby/groupby.py#L2877
# from rain.module_circular.array import Array
# from .array import Array


class GroupedArray(object):
    def __init__(self, array):
        self._groups = {}
        for elem in array:
            if elem in self._groups:
                self._groups[elem] += 1
            else:
                self._groups[elem] = 0

    def __repr__(self):
        return 'GroupedArray[{}]'.format(len(self._groups))

    def groups(self):
        # Importing Array here works because it does not interfere with
        # definition of GroupedArray.
        from rain.module_circular.array import Array
        return Array(self._groups.keys())
