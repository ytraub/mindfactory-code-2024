from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Side, Button, Color, Axis
from pybricks.tools import multitask, run_task, wait


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

    ###### < Movement > ######

    @control
    def run_drive_left(self, speed: int) -> None:
        self.drive_left_f.run(speed)

    @control
    def run_drive_right(self, speed: int) -> None:
        self.drive_right_b.run(speed)

    @control
    def run_module_left(self, speed: int) -> None:
        self.module_left_e.run(speed)

    @control
    def run_module_right(self, speed: int) -> None:
        self.module_right_a.run(speed);

    ###### < Stop > ######

    def stop_motors(self) -> None:
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

    def brake_drive_left(self) -> None:
        self.drive_left_f.brake()
        self.drive_left_f.brake()
        self.drive_left_f.brake()

    def brake_drive_right(self):
        self.drive_right_b.brake()
        self.drive_right_b.brake()
        self.drive_right_b.brake()

    def brake_module_left(self) -> None:
        self.module_left_e.brake()
        self.module_left_e.brake()
        self.module_left_e.brake()

    def brake_module_right(self) -> None:
        self.module_right_a.brake()
        self.module_right_a.brake()
        self.module_right_a.brake()

    ###### < Gyro > ######

    def get_gyro_angle(self) -> None:
        return self.hub.imu.heading()

    def reset_gyro_angle(self) -> None:
        self.hub.imu.reset_heading(0)

    ###### < Util > ######

    async def get_buttons(self) -> set[Button]:
        buttons = set()

        while not buttons:
            buttons = self.hub.buttons.pressed()
            await wait(50)

        while self.hub.buttons.pressed():
            await wait(50)

        return buttons
