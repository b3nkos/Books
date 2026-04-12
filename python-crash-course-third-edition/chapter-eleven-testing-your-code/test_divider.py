import pytest
from divider import divide

def test_divide_numbers():
    assert divide(10, 2)==5

def test_dive_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)