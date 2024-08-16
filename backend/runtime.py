class Chain:
    def __init__(self, start_task, label = "") -> None:
        self.label = label
        self.start_task = start_task


class Runtime:
    def __init__(self) -> None:
        self.tasks = []

    def get_tasks(self) -> list[any]:
        return self.tasks

    def set_tasks(self, state: list[any]) -> None:
        self.tasks = state

    def start(self, robot) -> None:
        while self.tasks:
            task = self.tasks.pop(0)
            task_finished = task.check()

            if task_finished:
                task.stop()

                next_tasks = task.get_next_tasks()
                if next_tasks:
                    self.add_tasks(next_tasks)
                else:
                    robot.end_run()
            else:
                self.tasks.append(task)

    def add_tasks(self, tasks: any | list[any]) -> None:
        if type(tasks) == list:
            for task in tasks:
                task.start()
                self.tasks.append(task)
        else:
            task = tasks

            task.start()
            self.tasks.append(task)
