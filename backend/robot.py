from pybricks.parameters import Side, Button, Color
from pybricks.tools import multitask, run_task, wait

from controller import Controller


class Robot:
    def __init__(self) -> None:
        self.controller = Controller()
        self.runs = []

    ###### < Util > ######

    def main(self) -> None:
        import runs

        self.runs = runs.runs
        self.setup()

        run_task(self.menu())

    def setup(self) -> None:
        self.controller.hub.display.orientation(Side.TOP)
        self.controller.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

        self.controller.reset_gyro_angle()
        self.controller.reset_motors()

    def check(self, arg: bool) -> bool:
        return arg and self.controller.get_running()

    async def menu(self) -> None:
        index = 0
        while True:
            if self.hub.imu.ready():
                self.hub.light.on(Color.GREEN)
            else:
                self.hub.light.on(Color.RED)

            self.hub.display.char(str(index + 1))
            buttons = await self.get_buttons()

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
                    self.execute_run(index)

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

        self.controller.reset_motors()
        self.controller.reset_gyro_angle()

    def end_run(self) -> None:
        self.controller.set_running(False)

        self.controller.brake_motors()
        self.controller.reset_motors()
        self.controller.reset_gyro_angle()

    ###### < Blocks > ######

    async def drive_forward(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        current_distance = 0
        self.controller.reset_drive(0)

        while self.check(current_distance <= distance):
            await multitask(
                self.controller.run_drive_left(speed),
                self.controller.run_drive_right(speed),
            )

            current_distance = self.controller.angle_drive_left()

        self.controller.brake_drive()

    async def drive_backward(self, speed: int, distance: int):
        speed = -abs(speed)
        distance = abs(distance)

        current_distance = 0
        self.controller.reset_drive(0)

        while self.check(current_distance <= distance):
            await multitask(
                self.controller.run_drive_left(speed),
                self.controller.run_drive_right(speed),
            )

            current_distance = self.controller.angle_drive_left()

        self.controller.brake_drive()

    async def module_left(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        current_distance = 0
        self.controller.reset_module_left(0)

        while self.check(current_distance <= distance):
            self.controller.run_module_left()
            current_distance = self.controller.angle_module_left()

        self.controller.brake_module_left()

    async def module_right(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        current_distance = 0
        self.controller.reset_module_right(0)

        while self.check(current_distance <= distance):
            self.controller.run_module_left()
            current_distance = self.controller.reset_module_right()

        self.controller.brake_module_right()

    async def turn_left(self, speed: int, angle: int):
        speed = abs(speed)
        target = -float(abs(angle))

        start_target = self.controller.get_gyro_angle()
        gyro_angle = self.controller.get_gyro_angle() - start_target

        while self.check(gyro_angle > target):
            gyro_angle = self.controller.get_gyro_angle() - start_target
            self.controller.run_drive_left(speed)

        self.controller.brake_drive_left()

    async def turn_right(self, speed: int, angle: int):
        speed = abs(speed)
        target = float(abs(angle))

        start_target = self.controller.get_gyro_angle()
        gyro_angle = self.controller.get_gyro_angle() - start_target

        while self.check(gyro_angle < target):
            gyro_angle = self.controller.get_gyro_angle() - start_target
            self.controller.run_drive_right(speed)

        self.controller.brake_drive_right()
