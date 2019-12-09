from __future__ import absolute_import  # No implicit relative imports
from __future__ import print_function
from __future__ import division
from builtins import range

from six import string_types

import pytest

# We use absolute non-full-path import here because we want to test things
# that we can reach from simply $REPO_ROOT/rain/__init__.py.
# We can also use absolute full-path import as well.
# Pandas does both of these things.
# Note: PyCharm does absolute non-full-path import by default.
from rain import banana


class TestModuleFruits:
    def test_banana(self):
        # Compatibility with Python 2 & 3
        assert isinstance(banana(), string_types)

        # In Python 3 only
        # assert isinstance(banana(), str)
