tasks = []

while True:
    task = input("Enter task (or type 'exit' to quit): ")

    if task.lower() == "exit":
        break

    tasks.append(task)

print("\nYour To-Do List:")

for i, task in enumerate(tasks, 1):
    print(i, task)