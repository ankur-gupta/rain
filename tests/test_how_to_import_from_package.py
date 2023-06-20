import pytest

# You can import from the package any way you want.
# Test a function that is intended to be used by the end user.
from rain import this_function_will_be_imported

# Test a function that is NOT intended to be used by the end user.
from rain.directory_module_with_selective_imports.utils import helper_function_1


def test_end_user_usable():
    assert isinstance(this_function_will_be_imported(), str)


def test_helper_function_1():
    assert helper_function_1() == 'helper_function_1'
