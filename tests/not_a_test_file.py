import pytest


# For pytest, the name of the
# 1. test file must begin with `test_`; a test file can contain functions that test multiple functions
# 2. function must begin with `test_`; a test function can contain tests for multiple functions
# 3. class must begin with `Test`
# 4. class methods must begin with `test_`


def this_is_also_not_a_test():
    # Since this is not a test file or a test function, the following assert statement won't fail
    assert 1 == 2


def test_this_will_not_be_tested():
    # Since this is not a test file, the following assert statement won't fail
    assert 1 == 2
