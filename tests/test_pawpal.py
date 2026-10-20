from pawpal_system import Task, Pet


def test_task_completion():
    task = Task(
        "Walk",
        "08:00",
        30
    )

    task.mark_complete()

    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Mochi", "Dog")
    task = Task("Feed", "09:00", 10)

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task