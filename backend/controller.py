from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait

SPEED_MULTIPLIER = 10


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

    ###### < Get / Set > ######

    def get_running(self) -> bool:
        return self.running

    def set_running(self, state: bool) -> None:
        self.running = state

    ###### < Movement > ######

    @control
    def run_drive_left(self, speed: int) -> None:
        self.drive_left_f.run(speed * SPEED_MULTIPLIER)

    @control
    def run_drive_right(self, speed: int) -> None:
        self.drive_right_b.run(speed * SPEED_MULTIPLIER)

    @control
    def run_module_left(self, speed: int) -> None:
        self.module_left_e.run(speed * SPEED_MULTIPLIER)

    @control
    def run_module_right(self, speed: int) -> None:
        self.module_right_a.run(speed * SPEED_MULTIPLIER)

    ###### < Stop > ######

    def brake_drive_left(self) -> None:
        self.drive_left_f.brake()
        self.drive_left_f.brake()
        self.drive_left_f.brake()

    def brake_drive_right(self) -> None:
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

    def brake_motors(self) -> None:
        self.brake_drive_left()
        self.brake_drive_right()
        self.brake_module_left()
        self.brake_module_right()

    def brake_drive(self) -> None:
        self.brake_drive_left()
        self.brake_drive_right()

    def brake_module(self) -> None:
        self.brake_module_left()
        self.brake_module_right()

    ###### < Reset > ######

    def reset_drive_left(self, angle: int) -> None:
        self.drive_left_f.reset_angle(angle)

    def reset_drive_right(self, angle: int) -> None:
        self.drive_right_b.reset_angle(angle)

    def reset_module_left(self, angle: int) -> None:
        self.module_left_e.reset_angle(angle)

    def reset_module_right(self, angle: int) -> None:
        self.module_right_a.reset_angle(angle)

    def reset_motors(self, angle: int) -> None:
        self.reset_drive_left(angle)
        self.reset_drive_right(angle)
        self.reset_module_left(angle)
        self.reset_module_right(angle)

    def reset_drive(self, angle: int) -> None:
        self.reset_drive_left(angle)
        self.reset_drive_right(angle)

    def reset_module(self, angle: int) -> None:
        self.reset_module_left(angle)
        self.reset_module_right(angle)

    ###### < Angle > ######

    def angle_drive_left(self) -> int:
        return self.drive_left_f.angle()

    def angle_drive_right(self) -> int:
        return self.drive_right_b.angle()

    def angle_module_left(self) -> int:
        return self.module_left_e.angle()

    def angle_module_right(self) -> int:
        return self.module_right_a.angle()

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
