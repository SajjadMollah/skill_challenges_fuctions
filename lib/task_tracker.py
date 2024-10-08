class Tracker:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def view_tasks(self):
        return self.tasks
    
    def complete_task(self, task):
        self.tasks.pop(task)
