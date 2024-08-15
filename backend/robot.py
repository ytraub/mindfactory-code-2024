from pybricks.parameters import Side, Button

from controller import Controller
from runtime import Runtime, Chain
from tasks import Tasks, Menu


class Robot:
    def __init__(self) -> None:
        self.runtime = Runtime()
        self.controller = Controller()
        self.tasks = Tasks(self, self.controller)

        self.running = False
        self.runs = []

    def get_running(self) -> bool:
        return self.running

    def set_running(self, state: bool) -> bool:
        self.running = state

    def main(self) -> None:
        self.load_runs()
        self.setup()

    def load_runs(self) -> None:
        from runs import __runs

        for run in __runs:
            run.create_chain(self)

    def setup(self) -> None:
        self.controller.hub.display.orientation(Side.TOP)
        self.controller.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

        self.controller.reset_gyro_angle(0)
        self.controller.reset_motors(0)

        self.runtime.add_tasks(self.tasks.menu())
        self.runtime.start(self)

    def execute_run(self, index: int) -> None:
        self.start_run()

        try:
            if index <= len(self.runs) - 1:
                run_chain = self.runs[index]
                self.runtime.add_tasks(run_chain.start_task)
            else:
                print(
                    f"Run: {index + 1} (index {index}) is not available. There are only {len(self.runs)} runs."
                )
        except Exception as err:
            print(f"An error occured while running: {err}")

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

    def chain(self, tasks: list[any | list[any]]) -> Chain:
        prev_task: any | None = None

        for task in reversed(tasks):
            if prev_task:
                if type(task) == list:
                    for _task in task:
                        _task.add_next_tasks(prev_task)
                else:
                    task.add_next_tasks(prev_task)

            prev_task = task

        self.runs.append(Chain(prev_task))
