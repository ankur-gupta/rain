import pytest

import rain


def test_version_exists():
    assert isinstance(rain.__version__, str)
