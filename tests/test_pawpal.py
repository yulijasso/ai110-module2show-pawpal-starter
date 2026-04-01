from pawpal_system import Task, Pet, Priority


def test_mark_complete():
    task = Task(name="Morning walk", duration=30, priority=Priority.HIGH, category="walk")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_count():
    pet = Pet(name="Buddy", species="Dog")
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task(name="Feed", duration=10, priority=Priority.HIGH, category="feeding"))
    assert len(pet.get_tasks()) == 1
    pet.add_task(Task(name="Walk", duration=30, priority=Priority.MEDIUM, category="walk"))
    assert len(pet.get_tasks()) == 2
