import pytest
from rain import demo_use_of_local_imports


def test_demo_use_of_local_imports():
    assert isinstance(demo_use_of_local_imports(), range)
