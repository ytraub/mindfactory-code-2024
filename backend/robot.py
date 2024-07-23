from pybricks.parameters import Port, Direction, Side, Button, Color, Axis
from pybricks.tools import multitask, run_task, wait

from controller import Controller

SPEED_MULTIPLIER = 10


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
        self.hub.display.orientation(Side.TOP)
        self.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

        self.reset_gyro_angle()

    def get_gyro_angle(self):
        return self.hub.imu.heading()

    def reset_gyro_angle(self):
        self.hub.imu.reset_heading(0)

    async def menu(self):
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

    async def get_buttons(self) -> set[Button]:
        buttons = set()

        while not buttons:
            buttons = self.hub.buttons.pressed()
            await wait(50)

        while self.hub.buttons.pressed():
            await wait(50)

        return buttons

    async def stop_motors(self):
        self.drive_left_f.brake()
        self.drive_left_f.brake()
        self.drive_left_f.brake()

        self.drive_right_b.brake()
        self.drive_right_b.brake()
        self.drive_right_b.brake()

        self.module_right_a.brake()
        self.module_right_a.brake()
        self.module_right_a.brake()

        self.module_left_e.brake()
        self.module_left_e.brake()
        self.module_left_e.brake()

    def brake_drive_right(self):
        self.drive_right_b.brake()
        self.drive_right_b.brake()
        self.drive_right_b.brake()

    def run_drive_left(self, speed: int):
        self.drive_left_f.run(speed)

    def brake_drive_left(self):
        self.drive_left_f.brake()
        self.drive_left_f.brake()
        self.drive_left_f.brake()

    async def drive_forward(self, speed: int, distance: int):
        speed = abs(speed) * SPEED_MULTIPLIER
        distance = abs(distance)

        await multitask(
            self.drive_right_b.run_target(speed, distance),
            self.drive_left_f.run_target(speed, distance),
        )

    async def drive_backward(self, speed: int, distance: int):
        speed = -(abs(speed) * SPEED_MULTIPLIER)
        distance = abs(distance)

        await multitask(
            self.drive_right_b.run_target(speed, distance),
            self.drive_left_f.run_target(speed, distance),
        )

    async def module_left(self, speed: int, distance: int):
        speed = abs(speed) * SPEED_MULTIPLIER
        distance = abs(distance)

        await self.module_left_e.run_target(speed, distance)
        self.module_left_e.brake()
        self.module_left_e.brake()
        self.module_left_e.brake()
        self.module_left_e.reset_angle(0)

    async def module_right(self, speed: int, distance: int):
        speed = abs(speed) * SPEED_MULTIPLIER
        distance = abs(distance)

        await self.module_right_a.run_target(speed, distance)
        self.module_right_a.brake()
        self.module_right_a.brake()
        self.module_right_a.brake()
        self.module_right_a.reset_angle(0)

    async def turn_left(self, speed: int, angle: int):
        speed = abs(speed) * SPEED_MULTIPLIER
        target = -float(abs(angle))

        start_target = self.get_gyro_angle()
        gyro_angle = self.get_gyro_angle() - start_target

        while gyro_angle > target:
            gyro_angle = self.get_gyro_angle() - start_target
            self.run_drive_right(speed)

        self.brake_drive_right()

    async def turn_right(self, speed: int, angle: int):
        speed = abs(speed) * SPEED_MULTIPLIER
        target = float(abs(angle))

        start_target = self.get_gyro_angle()
        gyro_angle = self.get_gyro_angle() - start_target

        while gyro_angle < target:
            gyro_angle = self.get_gyro_angle() - start_target
            self.run_drive_left(speed)

        self.brake_drive_right()
