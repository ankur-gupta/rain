from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

# Use "absolute full-path import" to import GroupedArray. See how
# rain/module_circular/group.py avoids circular imports.
from rain.module_circular.group import GroupedArray


class Array(object):
    def __init__(self, x):
        self._list = list(x)

    def __repr__(self):
        return 'Array[{}]'.format(len(self._list))

    def __getitem__(self, item):
        return self._list[item]

    def group(self):
        return GroupedArray(self)
