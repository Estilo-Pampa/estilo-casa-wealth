from task import Task
from task_manager import TaskManager

class UserInterface:
    def __init__(self):
        self.task_manager = TaskManager()
    
    def add_task(self):
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task = Task(task_name, task_description)
        self.task_manager.add_task(task)
    
    def remove_task(self):
        task_name = input("Enter task name: ")
        tasks = self.task_manager.get_tasks_by_status("Incomplete")
        for task in tasks:
            if task.name == task_name:
                self.task_manager.remove_task(task)
                break
    
    def view_tasks(self):
        tasks = self.task_manager.get_all_tasks()
        for task in tasks:
            print(task.name, task.description, task.status)
    
    def run(self):
        while True:
            print("1. Add task")
            print("2. Remove task")
            print("3. View tasks")
            print("4. Quit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.remove_task()
            elif choice == "3":
                self.view_tasks()
            elif choice == "4":
                break
