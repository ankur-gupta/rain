from __future__ import absolute_import  # No implicit relative imports
from __future__ import print_function
from __future__ import division
from builtins import range

import pytest
import numpy as np

# We use absolute non-full-path import here because we want to test things
# that we can reach from simply $REPO_ROOT/rain/__init__.py.
# We can also use absolute full-path import as well.
# Pandas does both of these things.
# Note: PyCharm does absolute non-full-path import by default.
from rain import function_three

RANDOM_SEED_NUMPY = 42
N_EXAMPLES = 10

# You can mark with multiple markers
@pytest.mark.random
@pytest.mark.sleepy
def test_function_three():
    np.random.seed(RANDOM_SEED_NUMPY)
    for _ in range(N_EXAMPLES):
        function_three()

