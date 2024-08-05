class Chain:
    def __init__(self, start_task) -> None:
        self.start_task = start_task


class Runtime:
    def __init__(self) -> None:
        self.tasks = []

    def start(self) -> None:
        while self.tasks:
            task = self.tasks.pop(0)
            task_finished = task.check()

            if task_finished:
                task.stop()

                self.add_tasks(task.get_next_tasks())
            else:
                self.tasks.append(task)

    def add_tasks(self, tasks: list[any]) -> None:
        for task in tasks:
            task.start()
            self.tasks.append(task)
