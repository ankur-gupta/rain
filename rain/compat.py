from __future__ import absolute_import  # No implicit relative imports


try:
    # Python 2
    from collections.abc import Iterable
except ImportError:
    # Python 3
    from collections import Iterable
