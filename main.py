from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Jordan")

mochi = Pet("Mochi", "Dog")
luna = Pet("Luna", "Cat")

owner.add_pet(mochi)
owner.add_pet(luna)


mochi.add_task(
    Task(
        "Evening walk",
        "18:00",
        30,
        "high",
        "daily",
        date.today()
    )
)

mochi.add_task(
    Task(
        "Breakfast",
        "08:00",
        10,
        "high",
        "daily",
        date.today()
    )
)

luna.add_task(
    Task(
        "Medication",
        "12:00",
        5,
        "high",
        "once",
        date.today()
    )
)

scheduler = Scheduler(owner)


print("Today's Schedule")
print("----------------")

for pet, task in scheduler.sort_by_time():
    print(
        f"{task.time} - {pet.name}: "
        f"{task.description} "
        f"({task.duration_minutes} min) "
        f"[{task.priority}]"
    )