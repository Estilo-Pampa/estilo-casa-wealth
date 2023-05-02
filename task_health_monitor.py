class TaskHealthMonitor:
    def __init__(self, tasks):
        self.tasks = tasks

    def get_overdue_tasks(self):
        today = datetime.date.today()
        overdue_tasks = []
        for task in self.tasks:
            if task.status != 'Completed' and task.end_date < today:
                overdue_tasks.append(task)
        return overdue_tasks

    def get_incomplete_tasks(self):
        incomplete_tasks = []
        for task in self.tasks:
            if task.status != 'Completed':
                incomplete_tasks.append(task)
        return incomplete_tasks

    def get_task_progress(self):
        completed_tasks = 0
        for task in self.tasks:
            if task.status == 'Completed':
                completed_tasks += 1
        return completed_tasks / len(self.tasks)
