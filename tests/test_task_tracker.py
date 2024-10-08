from lib.task_tracker import *

def test_add_task():
    tracker = Tracker()
    tracker.add_task("Clean room")
    result = tracker.view_tasks()
    assert result == ["Clean room"]

