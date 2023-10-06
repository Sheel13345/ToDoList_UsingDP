

# Caretaker class to manage tasks and undo/redo
class TaskManager:
    
    def __init__(self):
        self.tasks = []
        self.undo_stack = []
        self.redo_stack = []

    def add_task(self, task):
        self.tasks.append(task)
        self.undo_stack.append(task.create_memento())
        self.redo_stack.clear()

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                self.undo_stack.append(task.create_memento())
                self.redo_stack.clear()
                return

    def delete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                self.undo_stack.append(task.create_memento())
                self.redo_stack.clear()
                return

    def undo(self):
        if len(self.undo_stack) > 1:
            current_state = self.undo_stack.pop()
            self.redo_stack.append(current_state)
            previous_state = self.undo_stack[-1]
            for task in self.tasks:
                task.restore_from_memento(previous_state)

    def redo(self):
        if self.redo_stack:
            current_state = self.redo_stack.pop()
            self.undo_stack.append(current_state)
            for task in self.tasks:
                task.restore_from_memento(current_state)

    def view_tasks(self, filter_type):

        if filter_type == "sa":
            return self.tasks

        elif filter_type == "sc":
            return [task for task in self.tasks if task.completed]

        elif filter_type == "sp":
            return [task for task in self.tasks if not task.completed]
        else:
            return []
