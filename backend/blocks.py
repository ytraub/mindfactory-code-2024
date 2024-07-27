from pybricks.tools import multitask


class Blocks:
    def __init__(self, robot) -> None:
        self.robot = robot
        self.controller = robot.controller

    async def drive_forward(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        current_distance = 0
        self.controller.reset_drive(0)

        while self.robot.check(current_distance <= distance):
            await multitask(
                self.controller.run_drive_left(speed),
                self.controller.run_drive_right(speed),
            )

            current_distance = self.controller.angle_drive_left()

        self.controller.brake_drive()

    async def drive_backward(self, speed: int, distance: int):
        speed = -abs(speed)
        distance = abs(distance)

        current_distance = 0
        self.controller.reset_drive(0)

        while self.robot.check(current_distance <= distance):
            await multitask(
                self.controller.run_drive_left(speed),
                self.controller.run_drive_right(speed),
            )

            current_distance = self.controller.angle_drive_left()

        self.controller.brake_drive()

    async def module_left(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        current_distance = 0
        self.controller.reset_module_left(0)

        while self.robot.check(current_distance <= distance):
            self.controller.run_module_left()
            current_distance = self.controller.angle_module_left()

        self.controller.brake_module_left()

    async def module_right(self, speed: int, distance: int):
        speed = abs(speed)
        distance = abs(distance)

        current_distance = 0
        self.controller.reset_module_right(0)

        while self.robot.check(current_distance <= distance):
            self.controller.run_module_left()
            current_distance = self.controller.reset_module_right()

        self.controller.brake_module_right()

    async def turn_left(self, speed: int, angle: int):
        speed = abs(speed)
        target = -float(abs(angle))

        start_target = self.controller.get_gyro_angle()
        gyro_angle = self.controller.get_gyro_angle() - start_target

        while self.robot.check(gyro_angle > target):
            gyro_angle = self.controller.get_gyro_angle() - start_target
            self.controller.run_drive_left(speed)

        self.controller.brake_drive_left()

    async def turn_right(self, speed: int, angle: int):
        speed = abs(speed)
        target = float(abs(angle))

        start_target = self.controller.get_gyro_angle()
        gyro_angle = self.controller.get_gyro_angle() - start_target

        while self.robot.check(gyro_angle < target):
            gyro_angle = self.controller.get_gyro_angle() - start_target
            self.controller.run_drive_right(speed)

        self.controller.brake_drive_right()
