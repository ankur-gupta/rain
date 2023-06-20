import os
import logging

from rain.version import __version__
from rain.circular.array import Array
from rain.circular.grouped_array import GroupedArray

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
