class Task:
    def __init__(self) -> None:
        self.next_tasks = []

    def start(self):
        pass

    def check(self):
        return True

    def stop(self):
        pass

    def add_next_tasks(self, next_tasks):
        self.next_tasks.append(next_tasks)

    def get_next_tasks(self):
        return self.next_tasks


class Runtime:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def start(self) -> None:
        while self.tasks:
            task = self.tasks.pop(0)
            task_finished = task.check()

            if task_finished:
                task.stop()

                self.add_tasks(task.get_next_tasks())
            else:
                self.tasks.append(task)

    def add_tasks(self, tasks: list[Task]) -> None:
        for task in tasks:
            task.start()
            self.tasks.append(task)
