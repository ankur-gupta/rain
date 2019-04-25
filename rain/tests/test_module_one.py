from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from builtins import range

import pytest
from rain import function_one


class TestFunctionOne:
    x = 1

    def test_success(self):
        assert function_one() == 'one'

    def test_error(self):
        with pytest.raises(AssertionError):
            function_one(self.x)
