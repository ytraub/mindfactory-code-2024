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

    def main(self) -> None:
        import runs

        class_names = ["Test"]

        instances = {}

        for class_name in class_names:
            cls = getattr(runs, class_name, None)
            if cls:
                instances[class_name] = cls()

        run_task(instances["Test"].execute(self))

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

    async def module_right(self, speed: int, distance: int):
        speed = abs(speed) * SPEED_MULTIPLIER
        distance = abs(distance)

        await self.module_right_a.run_target(speed, distance)
