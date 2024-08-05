from pybricks.parameters import Side, Button, Color
from pybricks.tools import run_task, wait

from controller import Controller
from runtime import Runtime, Task
from tasks import Tasks


class Robot:
    def __init__(self) -> None:
        self.runtime = Runtime()
        self.controller = Controller()
        self.tasks = Tasks(self)

        self.runs = []

    def main(self) -> None:
        import runs

        self.runs = runs.runs
        self.setup()

        run_task(self.menu())

    def setup(self) -> None:
        self.controller.hub.display.orientation(Side.TOP)
        self.controller.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

        self.controller.reset_gyro_angle()
        self.controller.reset_motors(0)

    def check(self, arg: bool) -> bool:
        return arg and self.controller.get_running()

    async def menu(self) -> None:
        index = 0
        while True:
            if self.controller.hub.imu.ready():
                self.controller.hub.light.on(Color.GREEN)
            else:
                self.controller.hub.light.on(Color.RED)

            self.controller.hub.display.char(str(index + 1))
            buttons = await self.controller.get_buttons()

            if len(buttons) != 1:
                continue

            button = list(buttons)[0]
            if self.controller.get_running():
                if button == Button.CENTER:
                    self.end_run()
            else:
                if button == Button.RIGHT:
                    if index == len(self.runs) - 1:
                        index = 0
                    else:
                        index += 1
                elif button == Button.LEFT:
                    if index == 0:
                        index = len(self.runs) - 1
                    else:
                        index -= 1
                elif button == Button.CENTER:
                    await self.execute_run(index)

            await wait(100)

    async def execute_run(self, index: int) -> None:
        self.start_run()

        try:
            await self.runs[index].execute(self)
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

    def add_run(self, tasks: list[Task]):
        prev_task: Task | None = None
        for task in tasks:
            if prev_task:
                task.add_next_tasks([task])
            

