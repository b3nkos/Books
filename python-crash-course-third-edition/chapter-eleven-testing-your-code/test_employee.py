import pytest
from employee import Employee

@pytest.fixture
def employee():
    return Employee("jose", "martinez", 50000)


def test_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 55000


def test_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 60000
