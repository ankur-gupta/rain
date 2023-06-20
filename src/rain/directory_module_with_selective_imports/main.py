# Relative (local) imports from this module only
from .utils import helper_function_1, helper_function_2


def this_function_will_be_imported():
    return helper_function_1() + ", " + helper_function_2()
