from pybricks.tools import multitask


class Task:
    def __init__(self) -> None:
        self.next_tasks = []

    def __str__(self) -> str:
        return f"<Task next_tasks={self.next_tasks}>"

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


class DriveBackward(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = -abs(speed)
        self.distance = abs(distance)

    def start(self):
        self.controller.reset_drive(0)

    def check(self):
        self.current_distance = self.controller.angle_drive_left()
        self.controller.run_drive_left(self.speed)
        self.controller.run_drive_right(self.speed)
        return self.current_distance >= self.distance

    def stop(self):
        self.controller.brake_drive()


class ModuleLeft(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = abs(speed)
        self.distance = abs(distance)

    def start(self):
        self.controller.reset_module_left(0)

    def check(self):
        self.current_distance = self.controller.angle_module_left()
        self.controller.run_module_left(self.speed)
        return self.current_distance >= self.distance

    def stop(self):
        self.controller.brake_module_left()


class ModuleRight(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = abs(speed)
        self.distance = abs(distance)

    def start(self):
        self.controller.reset_module_right(0)

    def check(self):
        self.current_distance = self.controller.angle_module_right()
        self.controller.run_module_right(self.speed)
        return self.current_distance >= self.distance

    def stop(self):
        self.controller.brake_module_right()


class TurnLeft(Task):
    def __init__(self, controller, speed: int, angle: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = abs(speed)
        self.target = -float(abs(angle))
        self.start_target = self.controller.get_gyro_angle()

    def start(self):
        pass

    def check(self):
        gyro_angle = self.controller.get_gyro_angle() - self.start_target
        self.controller.run_drive_left(self.speed)
        return gyro_angle <= self.target

    def stop(self):
        self.controller.brake_drive_left()


class TurnRight(Task):
    def __init__(self, controller, speed: int, angle: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = abs(speed)
        self.target = float(abs(angle))
        self.start_target = self.controller.get_gyro_angle()

    def start(self):
        pass

    def check(self):
        gyro_angle = self.controller.get_gyro_angle() - self.start_target
        self.controller.run_drive_right(self.speed)
        return gyro_angle >= self.target

    def stop(self):
        self.controller.brake_drive_right()


class Tasks:
    def __init__(self, robot) -> None:
        self.robot = robot
        self.controller = robot.controller

    def drive_forward(self, speed: int, distance: int) -> DriveForward:
        return DriveForward(self.controller, speed=speed, distance=distance)

    def drive_backward(self, speed: int, distance: int) -> DriveBackward:
        return DriveBackward(self.controller, speed=speed, distance=distance)

    def module_left(self, speed: int, distance: int) -> ModuleLeft:
        return ModuleLeft(self.controller, speed=speed, distance=distance)

    def module_right(self, speed: int, distance: int) -> ModuleRight:
        return ModuleRight(self.controller, speed=speed, distance=distance)

    def turn_left(self, speed: int, angle: int) -> TurnLeft:
        return TurnLeft(self.controller, speed=speed, angle=angle)

    def turn_right(self, speed: int, angle: int) -> TurnRight:
        return TurnRight(self.controller, speed=speed, angle=angle)
