import pytest
import rain


def test_root():
    assert isinstance(rain._ROOT, str)
