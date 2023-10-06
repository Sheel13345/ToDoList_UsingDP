
from taskMemento import TaskMemento

# Task class with optional attributes using Builder Pattern
class Task:
    
    def __init__(self, description, due_date=None):
        self.description = description
        self.completed = False
        self.due_date = due_date

    def mark_completed(self):
        self.completed = True

    def mark_pending(self):
        self.completed = False

    def set_due_date(self, due_date):
        self.due_date = due_date

    def create_memento(self):
        return TaskMemento(self.description, self.completed, self.due_date)

    def restore_from_memento(self, memento):
        self.description = memento.description
        self.completed = memento.completed
        self.due_date = memento.due_date

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        return f"{self.description} [{status}{due_date_str}]"

