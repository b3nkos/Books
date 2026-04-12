import pytest
from manager import TaskManager


@pytest.fixture
def manager():
    manager = TaskManager()
    return manager


def test_add_task(manager):
    manager.add_task("study python")
    assert len(manager.tasks) == 1


def test_complete_task(manager):
    manager.add_task("study python")
    manager.complete_task(0)

    assert manager.tasks[0].completed is True


def test_invalid_task_index():
    manager = TaskManager()

    with pytest.raises(IndexError):
        manager.complete_task(0)
