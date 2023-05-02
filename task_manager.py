class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
    
    def get_all_tasks(self):
        return self.tasks
    
    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]
