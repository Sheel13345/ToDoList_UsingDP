

# Memento Pattern: Task Memento to store the state of a task
class TaskMemento:
    
    def __init__(self, description, completed, due_date):
        self.description = description
        self.completed = completed
        self.due_date = due_date