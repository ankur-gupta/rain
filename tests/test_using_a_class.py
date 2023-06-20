import pytest


class TestClassNoConstructor:
    # Setup anything that you need to test.
    x = 1

    def test_x_is_one(self):
        # Change this to `assert 1 == 2` to see that this method is indeed being tested
        assert self.x == 1


class TestClassWithConstructor:
    # Having a constructor means that this class won't be tested. Instead, you will see this warning:
    #
    # PytestCollectionWarning: cannot collect test class 'TestClassWithConstructor' because it has a
    # __init__ constructor (from: tests/test_using_a_class.py)
    #     class TestClassWithConstructor:
    #
    # -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
    def __init__(self, x: int):
        self.x = int(x)

    def test_will_not_run(self):
        # This test won't run because this class has a constructor
        assert 1 == 2
        