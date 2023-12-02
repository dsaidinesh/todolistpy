class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date=None, priority=None):
        task = {"description": description, "due_date": due_date, "priority": priority}
        self.tasks.append(task)

    def display_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['description']} - Due: {task['due_date']} - Priority: {task['priority']}")

        print("\nCompleted Tasks:")
        for i, task in enumerate(self.completed_tasks, start=1):
            print(f"{i}. {task['description']} - Due: {task['due_date']} - Priority: {task['priority']} (Completed)")

    def mark_as_completed(self, task_index):
        task = self.tasks.pop(task_index)
        self.completed_tasks.append(task)
        print(f"Task '{task['description']}' marked as completed.")

    def update_task(self, task_index, description=None, due_date=None, priority=None):
        task = self.tasks[task_index]
        if description:
            task['description'] = description
        if due_date:
            task['due_date'] = due_date
        if priority:
            task['priority'] = priority
        print("Task updated successfully.")

    def remove_task(self, task_index):
        task = self.tasks.pop(task_index)
        print(f"Task '{task['description']}' removed.")

todo_list = ToDoList()

while True:
    print("\n1. Add Task\n2. Display Tasks\n3. Mark as Completed\n4. Update Task\n5. Remove Task\n6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        description = input("Enter task description: ")
        due_date = input("Enter due date (optional): ")
        priority = input("Enter priority (optional): ")
        todo_list.add_task(description, due_date, priority)

    elif choice == "2":
        todo_list.display_tasks()

    elif choice == "3":
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        todo_list.mark_as_completed(task_index)

    elif choice == "4":
        task_index = int(input("Enter the task number to update: ")) - 1
        description = input("Enter updated description (press Enter to keep the same): ")
        due_date = input("Enter updated due date (press Enter to keep the same): ")
        priority = input("Enter updated priority (press Enter to keep the same): ")
        todo_list.update_task(task_index, description, due_date, priority)

    elif choice == "5":
        task_index = int(input("Enter the task number to remove: ")) - 1
        todo_list.remove_task(task_index)

    elif choice == "6":
        print("Exiting the To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
