from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction


def control(func):
    def wrapper(self, *args, **kwargs):
        if self.running:
            func(self, *args, **kwargs)

    return wrapper


class Controller:
    def __init__(self) -> None:
        self.hub = PrimeHub()

        self.running = False

        self.drive_right_b = Motor(Port.B, Direction.CLOCKWISE)
        self.drive_left_f = Motor(Port.F, Direction.COUNTERCLOCKWISE)
        self.module_right_a = Motor(Port.A)
        self.module_left_e = Motor(Port.E)
        self.module_color_c = ColorSensor(Port.C)

    @control
    def run_drive_right(self, speed: int) -> None:
        self.drive_right_b.run(speed)
