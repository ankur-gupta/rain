import pytest
from rain import a_function_in_a_submodule


def test_a_function_in_a_submodule():
    assert a_function_in_a_submodule() == "a_function_in_a_submodule"
