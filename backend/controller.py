from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Button

SPEED_MULTIPLIER = 10


class Controller:
    def __init__(self) -> None:
        self.hub = PrimeHub()

        self.drive_left_b = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.drive_right_e = Motor(Port.E, Direction.CLOCKWISE)
        self.module_left_a = Motor(Port.A)
        self.module_right_f = Motor(Port.F)
        self.module_color_d = ColorSensor(Port.D)
        self.ground_color_c = ColorSensor(Port.C)

        self.gyro_offset_angle = self.get_gyro_raw_angle()

    ###### < Movement > ######

    def run_drive_left(self, speed: int) -> None:
        self.drive_left_b.run(speed * SPEED_MULTIPLIER)

    def run_drive_right(self, speed: int) -> None:
        self.drive_right_e.run(speed * SPEED_MULTIPLIER)

    def run_module_left(self, speed: int) -> None:
        self.module_right_f.run(speed * SPEED_MULTIPLIER)

    def run_module_right(self, speed: int) -> None:
        self.module_left_a.run(speed * SPEED_MULTIPLIER)

    ###### < Stop > ######

    def brake_drive_left(self) -> None:
        self.drive_left_b.brake()
        self.drive_left_b.brake()
        self.drive_left_b.brake()

    def brake_drive_right(self) -> None:
        self.drive_right_e.brake()
        self.drive_right_e.brake()
        self.drive_right_e.brake()

    def brake_module_left(self) -> None:
        self.module_right_f.brake()
        self.module_right_f.brake()
        self.module_right_f.brake()

    def brake_module_right(self) -> None:
        self.module_left_a.brake()
        self.module_left_a.brake()
        self.module_left_a.brake()

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
        self.drive_left_b.reset_angle(angle)

    def reset_drive_right(self, angle: int) -> None:
        self.drive_right_e.reset_angle(angle)

    def reset_module_left(self, angle: int) -> None:
        self.module_right_f.reset_angle(angle)

    def reset_module_right(self, angle: int) -> None:
        self.module_left_a.reset_angle(angle)

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
        return self.drive_left_b.angle()

    def angle_drive_right(self) -> int:
        return self.drive_right_e.angle()

    def angle_module_left(self) -> int:
        return self.module_right_f.angle()

    def angle_module_right(self) -> int:
        return self.module_left_a.angle()

    ###### < Gyro > ######

    def get_gyro_angle(self) -> float:
        return self.hub.imu.heading() - self.gyro_offset_angle

    def get_gyro_raw_angle(self) -> float:
        return self.hub.imu.heading()
    
    def reset_gyro(self) -> None:
        self.gyro_offset_angle = self.get_gyro_raw_angle()

    def reset_gyro_angle(self, angle: int) -> None:
        self.hub.imu.reset_heading(angle)

    ###### < Util > ######

    def get_buttons(self) -> set[Button]:
        return self.hub.buttons.pressed()
