import pytest
from rain import this_function_will_be_imported


def test_this_function_will_be_imported():
    assert isinstance(this_function_will_be_imported(), str)
