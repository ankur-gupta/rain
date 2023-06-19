# This will cause a circular import error:
# from rain.circular.array import Array
# ImportError: cannot import name 'Array' from partially initialized module 'rain.circular.array'
# (most likely due to a circular import) (.../lib/python3.11/site-packages/rain/circular/array.py).

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

    def groups(self):
        # Importing Array here works because it does not interfere with definition of GroupedArray
        # Pandas solves this issue the same way. See this line:
        # https://github.com/pandas-dev/pandas/blob/80ba4c4294a1ce1d95aeeb8e5de86d33ebb6edf4/pandas/core/groupby/groupby.py#L2877
        from rain.circular.array import Array
        return Array(self._groups.keys())
