import pytest


# For pytest, the name of the
# 1. test file must begin with `test_`; a test file can contain functions that test multiple functions
# 2. function must begin with `test_`; a test function can contain tests for multiple functions
# 3. class must begin with `Test`
# 4. class methods must begin with `test_`


def this_is_not_a_test():
    # Since this is not a test function, the following assert statement won't be tested
    assert 1 == 2


def test_this_is_a_test():
    # Try changing this to `assert 1 == 2` to see that something is indeed being tested
    assert 1 == 1


class ThisIsNotATestClass:
    def test_method(self):
        # Since this is not a test class, the following assert statement won't be tested
        assert 1 == 2


class TestClass:
    def this_is_not_a_test_method(self):
        # Since this is not a test method, the following assert statement won't be tested
        assert 1 == 2

    def test_method(self):
        # Try changing this to `assert 1 == 2` to see that this method is indeed being tested
        assert 1 == 1
