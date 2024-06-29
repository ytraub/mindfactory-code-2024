from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Side, Button
from pybricks.tools import multitask, run_task, wait

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
        run_task(self.menu())

    def setup(self) -> None:
        self.hub.display.orientation(Side.TOP)
        self.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

    async def menu(self):
        index = 0
        while True:
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

            await wait(100)

    async def get_buttons(self) -> set[Button]:
        buttons = set()

        while not buttons:
            buttons = self.hub.buttons.pressed()
            await wait(50)

        while self.hub.buttons.pressed():
            await wait(50)

        return buttons

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
