from pybricks.parameters import Side, Button, Color
from pybricks.tools import multitask, run_task, wait

from controller import Controller


class Robot:
    def __init__(self) -> None:
        self.controller = Controller()
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
        self.controller.running = True

        try:
            await self.runs[index].execute(self)
            await self.stop_motors()
        except Exception as err:
            print(f"An error occured while running: {err}")

        self.controller.running = False

    async def drive_forward(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        current_distance = 0

        await multitask(
            self.drive_right_b.run_target(speed, distance),
            self.drive_left_f.run_target(speed, distance),
        )

    async def drive_backward(self, speed: int, distance: int):
        speed = -abs(speed)
        distance = abs(distance)

        await multitask(
            self.drive_right_b.run_target(speed, distance),
            self.drive_left_f.run_target(speed, distance),
        )

    async def module_left(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        await self.module_left_e.run_target(speed, distance)
        self.module_left_e.brake()
        self.module_left_e.brake()
        self.module_left_e.brake()
        self.module_left_e.reset_angle(0)

    async def module_right(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        await self.module_right_a.run_target(speed, distance)
        self.module_right_a.brake()
        self.module_right_a.brake()
        self.module_right_a.brake()
        self.module_right_a.reset_angle(0)

    async def turn_left(self, speed: int, angle: int):
        speed = abs(speed)
        target = -float(abs(angle))

        start_target = self.get_gyro_angle()
        gyro_angle = self.get_gyro_angle() - start_target

        while gyro_angle > target:
            gyro_angle = self.get_gyro_angle() - start_target
            self.run_drive_right(speed)

        self.brake_drive_right()

    async def turn_right(self, speed: int, angle: int):
        speed = abs(speed)
        target = float(abs(angle))

        start_target = self.get_gyro_angle()
        gyro_angle = self.get_gyro_angle() - start_target

        while gyro_angle < target:
            gyro_angle = self.get_gyro_angle() - start_target
            self.run_drive_left(speed)

        self.brake_drive_right()
