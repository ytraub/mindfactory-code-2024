from pybricks.parameters import Side, Button

from controller import Controller
from runtime import Runtime, Chain
from tasks import Tasks, Task


class Robot:
    def __init__(self) -> None:
        self.runtime = Runtime()
        self.controller = Controller()
        self.tasks = Tasks(self, self.controller)

        self.running = False
        self.loading = False

        self.runs = []

    def get_running(self) -> bool:
        return self.running

    def set_running(self, state: bool) -> None:
        self.running = state

    def get_loading(self) -> bool:
        return self.loading

    def set_loading(self, state: bool) -> None:
        self.loading = state

    def main(self) -> None:
        self.load_runs()
        self.setup()

    def load_runs(self) -> None:
        self.set_loading(True)
        self.runs.clear()

        self.chain([self.tasks.start_run_with_color()], "")

        from runs import __runs__

        for run in __runs__:
            run.create_chain(self)

        self.set_loading(False)

    def setup(self) -> None:
        self.controller.hub.display.orientation(Side.TOP)
        self.controller.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

        self.controller.reset_gyro_angle(0)
        self.controller.reset_motors(0)

        self.runtime.add_tasks(self.tasks.menu())
        self.runtime.start(self)

    def execute_run(self, index: int) -> None:
        self.start_run()

        if index <= len(self.runs) - 1:
            run_chain = self.runs[index]
            self.runtime.add_tasks(run_chain.start_task)
        else:
            print(
                f"Run: {index + 1} (index {index}) is not available. There are only {len(self.runs)} runs."
            )

    def interrupt_run(self) -> None:
        self.runtime.tasks.clear()
        self.end_run()

    def start_run(self) -> None:
        self.set_running(True)

        self.controller.reset_motors(0)

    def end_run(self) -> None:
        self.set_running(False)

        self.controller.brake_motors()
        self.controller.reset_motors(0)

    def chain(self, tasks: list[Task | list[Task]], run_color: str) -> None:
        start_task: Task | None = None
        previous_task: Task | None = None
        tasksplit_start_tasks: list[Task] = []

        for task in tasks:
            if isinstance(task, list):
                tasksplit_start_task: Task | None = None
                tasksplit_previous_task: Task | None = None

                for tasksplit_task in task:
                    if not tasksplit_start_task:
                        tasksplit_start_task = tasksplit_task

                    if tasksplit_previous_task:
                        tasksplit_previous_task.set_next_tasks(tasksplit_task)

                    tasksplit_previous_task = tasksplit_task

                tasksplit_start_tasks.append(tasksplit_start_task)
            else:
                if not start_task:
                    start_task = task

                if previous_task:
                    if tasksplit_start_tasks:
                        previous_task.set_next_tasks([task] + tasksplit_start_tasks)
                        tasksplit_start_tasks.clear()
                    else:
                        previous_task.set_next_tasks(task)

                previous_task = task

        self.runs.append(Chain(start_task, run_color))
