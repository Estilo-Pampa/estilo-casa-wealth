class Project:
    def __init__(self, name, tasks, start_date, end_date, budget):
        self.name = name
        self.tasks = tasks
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

class Task:
    def __init__(self, name, description, assigned_to, status, start_date, end_date, estimated_hours, actual_hours):
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.estimated_hours = estimated_hours
        self.actual_hours = actual_hours
