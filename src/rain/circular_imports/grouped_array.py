# This will cause a circular import error:
# # from rain.circular_imports.array import Array
# ImportError: cannot import name 'Array' from partially initialized module 'rain.circular_imports.array'
# (most likely due to a circular import) (.../lib/python3.11/site-packages/rain/circular_imports/array.py).

# This will let the type hint reference to Array work as long as you import Array at the end of this file.
from __future__ import annotations


class GroupedArray:
    """ Returns value-counts over an Array object """

    def __init__(self, array):
        self._groups = {}
        for e in array:
            if e in self._groups:
                self._groups[e] += 1
            else:
                self._groups[e] = 1

    def __repr__(self):
        return f'{self.__class__.__name__}{repr(self._groups)}'

    # The type hint references 'Array' which is not yet imported. To solve this,
    # 1. import `annotations` from `__future__`
    # 2. import `Array` at the end of this file
    def groups(self) -> Array:
        # This import wouldn't solve the NameError (undefined 'Array' problem) in the type hint.
        # As a result, we import Array at the end of the file.
        # Importing Array here works because it does not interfere with definition of GroupedArray
        # Pandas solves this issue the same way. See this line:
        # https://github.com/pandas-dev/pandas/blob/80ba4c4294a1ce1d95aeeb8e5de86d33ebb6edf4/pandas/core/groupby/groupby.py#L2877
        # from rain.circular_imports.array import Array
        return Array(self._groups.keys())


# Import here to avoid circular imports
# https://github.com/ankur-gupta/rain/tree/v1#circular-imports-or-dependencies
# This along with importing `annotations` from `__future__` will fix let us use Array in the type hint.
# Use a local import instead of a package-level import: from rain.circular_imports.array import Array
from .array import Array
