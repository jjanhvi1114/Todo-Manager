import json
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, category="", priority="", due_date="", status="Pending"):
        self.tasks.append({"task": task, "category": category, "priority": priority, "due_date": due_date, "status": status})
        print(f"Task '{task}' added.")


    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task index.")

    def view_tasks(self, category=None, status=None):
        filtered_tasks = self.tasks
        if category:
            filtered_tasks = [task for task in filtered_tasks if task["category"] == category]
        if status:
            filtered_tasks = [task for task in filtered_tasks if task["status"] == status]

        if filtered_tasks:
            print("Tasks:")
            for index, task in enumerate(filtered_tasks, start=1):
                print(f"{index}. {task['task']} | Category: {task['category']} | Priority: {task['priority']} | Due Date: {task['due_date']} | Status: {task['status']}")
        else:
            print("No tasks.")

    def update_task_status(self, task_index, status):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["status"] = status
            print(f"Task status updated to '{status}'.")
        else:
            print("Invalid task index.")

    def save_tasks(self, file_name="tasks.json"):
        with open(file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)
        print("Tasks saved successfully.")

    def load_tasks(self, file_name="tasks.json"):
        try:
            with open(file_name, "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved tasks found.")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task as Done")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            category = input("Enter category (optional): ")
            priority = input("Enter priority (optional): ")
            due_date = input("Enter due date (YYYY-MM-DD format, optional): ")
            todo_list.add_task(task, category, priority, due_date)
        elif choice == "2":
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index - 1)
        elif choice == "3":
            category = input("Enter category to filter (optional): ")
            status = input("Enter status to filter (optional): ")
            todo_list.view_tasks(category, status)
        elif choice == "4":
            task_index = int(input("Enter task index to mark as done: "))
            todo_list.update_task_status(task_index - 1, "Done")
        elif choice == "5":
            todo_list.save_tasks()
        elif choice == "6":
            todo_list.load_tasks()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
