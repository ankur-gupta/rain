from rain.circular.grouped_array import GroupedArray


class Array:
    """ A simple wrapper over list """
    def __init__(self, data):
        self._list = list(data)

    def __repr__(self):
        return f'{self.__class__.__name__}{repr(self._list)}'

    def __getitem__(self, item):
        return self._list[item]

    def group(self):
        return GroupedArray(self)
