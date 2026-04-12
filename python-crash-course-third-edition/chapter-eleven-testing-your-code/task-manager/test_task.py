from task import Task

def test_task_completion():
    task=Task("Study Python")
    task.complete()
    
    assert task.completed is True