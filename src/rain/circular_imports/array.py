# This will cause a circular import error:
# # from rain.circular_imports.grouped_array import GroupedArray
# ImportError: cannot import name 'Array' from partially initialized module 'rain.circular_imports.array'
# (most likely due to a circular import) (rain/src/rain/circular_imports/array.py)

# This will let the type hint reference to Array work as long as you import GroupedArray at the end of this file.
from __future__ import annotations

class Array:
    """ A simple wrapper over list """

    def __init__(self, data):
        self._list = list(data)

    def __repr__(self):
        return f'{self.__class__.__name__}{repr(self._list)}'

    def __getitem__(self, item):
        return self._list[item]

    # The type hint references 'Array' which is not yet imported. To solve this,
    # 1. import `annotations` from `__future__`
    # 2. import `GroupedArray` at the end of this file
    def group(self) -> GroupedArray:
        return GroupedArray(self)


# Import here to avoid circular imports
# https://github.com/ankur-gupta/rain/tree/v1#circular-imports-or-dependencies
# This along with importing `annotations` from `__future__` will fix let us use Array in the type hint.
# Use a local import instead of a package-level import: from rain.circular_imports.grouped_array import GroupedArray
from .grouped_array import GroupedArray