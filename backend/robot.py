from pybricks.parameters import Side, Button, Color

from controller import Controller
from runtime import Runtime, Chain
from tasks import Tasks


class Robot:
    def __init__(self) -> None:
        self.runtime = Runtime()
        self.controller = Controller()
        self.tasks = Tasks(self)

        self.running = False

        self.runs = []

    def get_running(self) -> bool:
        return self.running

    def set_running(self, state: bool) -> bool:
        self.running = state

    def main(self) -> None:
        from runs import __runs

        for run in __runs:
            run.create_chain(self)

        self.setup()

    def setup(self) -> None:
        self.controller.hub.display.orientation(Side.TOP)
        self.controller.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

        self.controller.reset_gyro_angle()
        self.controller.reset_motors(0)

    def execute_run(self, index: int) -> None:
        self.start_run()

        try:
            self.runs[index].execute(self)
        except Exception as err:
            print(f"An error occured while running: {err}")

        self.end_run()

    def start_run(self) -> None:
        self.controller.set_running(True)

        self.controller.reset_motors(0)
        self.controller.reset_gyro_angle()

    def end_run(self) -> None:
        self.controller.set_running(False)

        self.controller.brake_motors()
        self.controller.reset_motors(0)
        self.controller.reset_gyro_angle()

    def chain(self, tasks: list[any | list[any]]) -> Chain:
        prev_task: any | None = None

        for task in reversed(tasks):
            if prev_task:
                task.add_next_tasks(task)

            prev_task = task

        self.runs.append(Chain(prev_task))
