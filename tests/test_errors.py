import pytest
import random


def test_assertion_error():
    with pytest.raises(AssertionError):
        # Change this to `assert 1 == 2` to check that this test is being run as you expect
        assert 1 == 2


def test_general_error():
    # We run this test many times to (hopefully) verify that we can catch either error.
    for _ in range(1000):
        with pytest.raises(Exception):
            # We will either get an AssertionError or a ValueError with 50-50 chance.
            if random.random() < 0.5:
                assert 1 == 2
            else:
                raise ValueError('Received an unexpected value')
