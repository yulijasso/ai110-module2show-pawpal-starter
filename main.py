from pawpal_system import Owner, Pet, Task, Priority, Scheduler

# Create owner
owner = Owner("Yuli", available_time=90)

# Create pets
dog = Pet("Buddy", "Dog", "Golden Retriever", 3)
cat = Pet("Mimi", "Cat", "Siamese", 2)

owner.add_pet(dog)
owner.add_pet(cat)

# Add tasks
dog.add_task(Task("Morning walk", 30, Priority.HIGH, "walk"))
dog.add_task(Task("Give heartworm med", 5, Priority.HIGH, "meds"))
dog.add_task(Task("Brush coat", 15, Priority.LOW, "grooming"))

cat.add_task(Task("Feed breakfast", 10, Priority.HIGH, "feeding"))
cat.add_task(Task("Play with feather toy", 20, Priority.MEDIUM, "enrichment"))
cat.add_task(Task("Clean litter box", 10, Priority.MEDIUM, "grooming"))

# Generate and print schedule
scheduler = Scheduler(owner)
print("=" * 50)
print("  PawPal+ — Today's Schedule")
print("=" * 50)
print()
print(scheduler.get_explanation())
