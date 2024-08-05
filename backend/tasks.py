from pybricks.tools import multitask


class Task:
    def __init__(self) -> None:
        self.next_tasks = []

    def start(self):
        pass

    def check(self):
        return True

    def stop(self):
        pass

    def add_next_tasks(self, tasks):
        if type(tasks) == list:
            self.next_tasks.extend(tasks)
        else:
            self.next_tasks.append(tasks)

    def get_next_tasks(self):
        return self.next_tasks


class DriveForward(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller

        self.speed = abs(speed)
        self.distance = abs(distance)

        self.current_distance = 0

    def start(self):
        self.controller.reset_drive(0)

    def check(self):
        self.controller.run_drive_left(self.speed),
        self.controller.run_drive_right(self.speed)

        return self.current_distance >= self.distance

    def stop(self):
        self.controller.brake_drive()


class Tasks:
    def __init__(self, robot) -> None:
        self.robot = robot
        self.controller = robot.controller

    def drive_forward(self, speed: int, distance: int) -> DriveForward:
        return DriveForward(self.controller, speed=speed, distance=distance)

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
