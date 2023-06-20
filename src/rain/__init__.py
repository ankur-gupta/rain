import os
import logging

from rain.version import __version__

# File and directory level modules
from rain.this_file_is_a_module import a_function_in_a_module
from rain.this_directory_is_a_module.this_file_is_a_submodule import a_function_in_a_submodule

# Filtered imports from a directory-level module
# See $REPO_ROOT/src/rain/directory_module_with_selective_imports/__init__.py for detailed explanation.
from rain.directory_module_with_selective_imports import this_function_will_be_imported

# Demo of local imports
from rain.local_imports.main import demo_use_of_local_imports

# Circular imports
from rain.circular_imports.array import Array
from rain.circular_imports.grouped_array import GroupedArray

# Logging demo
from rain.logging_example.main import logger_demo

# Define a logger for the whole package. See:
# https://realpython.com/python-logging-source-code/#library-vs-application-logging-what-is-nullhandler
# https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
# https://stackoverflow.com/questions/27016870/how-should-logging-be-used-in-a-python-package
logging.getLogger(__name__).addHandler(logging.NullHandler())


_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_path(partial_path=''):
    return os.path.join(_ROOT, partial_path)


def load_mathematicians(partial_path='resources/mathematicians.txt'):
    path = get_path(partial_path)
    with open(path, 'r') as f:
        mathematicians = f.readlines()
    mathematicians = [m.strip() for m in mathematicians]
    return mathematicians
