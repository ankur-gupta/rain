from __future__ import absolute_import  # No implicit relative imports
from __future__ import print_function
from __future__ import division
from builtins import range

import pytest

# We use absolute non-full-path import here because we want to test things
# that we can reach from simply $REPO_ROOT/rain/__init__.py.
# We can also use absolute full-path import as well.
# Pandas does both of these things.
# Note: PyCharm does absolute non-full-path import by default.
from rain import function_one, function_two


class TestFunctionOne:
    x = 1

    def test_success(self):
        assert function_one() == 'one'

    # Tests marked as "sleepy". This can be anything you want.
    # See http://doc.pytest.org/en/latest/example/markers.html
    @pytest.mark.sleepy
    def test_error(self):
        with pytest.raises(AssertionError):
            function_one(self.x)


@pytest.mark.sleepy
class TestFunctionTwo:
    x = 1

    def test_function_two(self):
        assert function_two(self.x) == function_one()
