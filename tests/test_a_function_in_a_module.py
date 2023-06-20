import pytest
from rain import a_function_in_a_module


def test_a_function_in_a_module():
    assert a_function_in_a_module() == "a_function_in_a_module"