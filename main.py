
from datetime import datetime

from task import Task
from taskManager import TaskManager


# Helper function to create a Task using Builder Pattern
def create_task(description, due_date=None):
    
    task_builder = Task(description, due_date)
    return task_builder

# Main function to interact with the To-Do List Manager


def main():

    task_manager = TaskManager()

    while True:

        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Completed")
        print("3. Delete Task")
        print("4. Undo")
        print("5. Redo")
        print("6. View Tasks")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")

            if due_date:
                due_date = datetime.strptime(due_date, "%Y-%m-%d")

            task = create_task(description, due_date)
            task_manager.add_task(task)
            print(f"Task '{description}' added.")

        elif choice == "2":
            description = input(
                "Enter task description to mark as completed: ")
            
            task_manager.mark_completed(description)
            print(f"Task '{description}' marked as completed.")

        elif choice == "3":
            description = input("Enter task description to delete: ")
            task_manager.delete_task(description)
            print(f"Task '{description}' deleted.")

        elif choice == "4":
            task_manager.undo()
            print("Undo completed.")

        elif choice == "5":
            task_manager.redo()
            print("Redo completed.")

        elif choice == "6":
            filter_type = input(
                # "Enter filter type (Show all/Show completed/Show pending): ")
                "Enter filter type (sa (for Show all)/sc (for Show completed)/sp (for Show pending)): ")
            tasks = task_manager.view_tasks(filter_type)

            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
