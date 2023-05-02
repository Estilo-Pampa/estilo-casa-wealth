class DailyMonitor:
    def __init__(self, tasks, finance_manager):
        self.tasks = tasks
        self.finance_manager = finance_manager

    def print_task_health_report(self):
        overdue_tasks = TaskHealthMonitor(self.tasks).get_overdue_tasks()
        incomplete_tasks = TaskHealthMonitor(self.tasks).get_incomplete_tasks()
        task_progress = TaskHealthMonitor(self.tasks).get_task_progress()

        print("Task Health Report:")
        print("Overdue tasks:")
        for task in overdue_tasks:
            print(f"- {task.name}")
        print("Incomplete tasks:")
        for task in incomplete_tasks:
            print(f"- {task.name}")
        print(f"Task progress: {task_progress:.2%}")

    def print_finance_report(self):
        total_expenses = self.finance_manager.get_total_expenses()
        budget_status = self.finance_manager.get_budget_status()

        print("Finance Report:")
        print(f"Total expenses: ${total_expenses:.2f}")
        print(f"Budget status: ${budget_status:.2f}")
