import pytest


# For pytest, the name of the
# 1. test file must begin with `test_`
# 2. function must begin with `test_`
# 3. class must begin with `Test`
# 4. class methods must begin with `test_`


def this_is_not_a_test():
    # Since this is not a test function, the following assert statement won't fail
    assert 1 == 2


def test_this_is_a_test():
    # Try changing this to `assert 1 == 2` to see that something is indeed being tested
    assert 1 == 1


