from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for item in self.tasks:
            if item.name == task_name:
                item.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared = 0
        for task in self.tasks:
            if task.completed:
                cleared += 1
                self.tasks.remove(task)
        return f"Cleared {cleared} tasks."

    def view_section(self):
        to_print = ''
        for task in self.tasks:
            to_print += f'{task.details()} \n'
        return f"Section {self.name}: \n" \
               f"{to_print}"