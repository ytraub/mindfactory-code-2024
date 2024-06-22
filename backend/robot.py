from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import multitask, run_task

SPEED_MULTIPLIER = 10


class Robot:
    def __init__(self) -> None:
        self.hub = PrimeHub()

        self.drive_right_b = Motor(Port.B, Direction.CLOCKWISE)
        self.drive_left_f = Motor(Port.F, Direction.COUNTERCLOCKWISE)
        self.module_right_a = Motor(Port.A)
        self.module_left_e = Motor(Port.E)
        self.module_color_c = ColorSensor(Port.C)

    async def run_drive_target_forward(self, speed: int, target: int):
        speed = abs(speed) * SPEED_MULTIPLIER
        target = abs(target)

        await multitask(
            self.drive_right_b.run_target(speed, target),
            self.drive_left_f.run_target(speed, target),
        )

    async def run_drive_target_backward(self, speed: int, target: int):
        speed = -(abs(speed) * SPEED_MULTIPLIER)
        target = abs(target)

        await multitask(
            self.drive_right_b.run_target(speed, target),
            self.drive_left_f.run_target(speed, target),
        )
