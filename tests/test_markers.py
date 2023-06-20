import pytest
import time
import random


@pytest.mark.slow
def test_slow():
    # This test is takes a long time. This is why we marked it as slow.
    # Now, we can deselect this test when testing other things.
    time.sleep(1)
    assert 1 == 1
    time.sleep(1)


@pytest.mark.random
def test_random():
    n = 100_000
    x_sum = 0
    for _ in range(n):
        x_sum += random.random()
    mean = x_sum / float(n)
    error = abs(mean - 0.5)

    # This test will pass sometimes but not everytime.
    # This is why we marked it as random.
    # Now, we can deselect this test when testing other things.
    assert error <= 1e-3

