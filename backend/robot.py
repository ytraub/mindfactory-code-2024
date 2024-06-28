from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Side, Button
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

        self.runs = []

    def main(self) -> None:
        import runs

        self.runs = runs.runs
        self.setup()
        #run_task(self.menu())

    def setup(self) -> None:
        self.hub.display.orientation(Side.TOP)

    async def menu(self):
        index = 0
        while True:
            buttons = self.hub.buttons.pressed()

            if len(buttons) != 1:
                continue

            button = buttons.pop()
            match button:
                case Button.LEFT:
                    index -= 1
                case Button.RIGHT:
                    index += 1

            self.hub.display.number(index)

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
