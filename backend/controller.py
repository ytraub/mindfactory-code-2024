from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction


class Controller:
    def __init__(self):
        self.hub = PrimeHub()

        self.drive_right_b = Motor(Port.B, Direction.CLOCKWISE)
        self.drive_left_f = Motor(Port.F, Direction.COUNTERCLOCKWISE)
        self.module_right_a = Motor(Port.A)
        self.module_left_e = Motor(Port.E)
        self.module_color_c = ColorSensor(Port.C)
