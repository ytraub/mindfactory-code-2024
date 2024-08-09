from pybricks.parameters import Side, Button, Color


class Task:
    def __init__(self) -> None:
        self.next_tasks = []

    def __str__(self) -> str:
        return f"<Task next_tasks={self.next_tasks}>"

    def start(self) -> None:
        pass

    def check(self) -> bool:
        return True

    def stop(self) -> None:
        pass

    def add_next_tasks(self, tasks: any | list[any]) -> None:
        if type(tasks) == list:
            self.next_tasks.extend(tasks)
        else:
            self.next_tasks.append(tasks)

    def get_next_tasks(self) -> None:
        return self.next_tasks


class Menu(Task):
    def __init__(self, robot, controller) -> None:
        super().__init__()
        self.robot = robot
        self.controller = controller

        self.run_index = 0

    def check(self) -> bool:
        if self.controller.hub.imu.ready():
            self.controller.hub.light.on(Color.GREEN)
        else:
            self.controller.hub.light.on(Color.RED)

        self.controller.hub.display.char(str(self.run_index + 1))

        buttons = self.controller.get_buttons()
        if len(buttons) == 1:
            self.handle_button(list(buttons)[0])

        return False

    def handle_button(self, button: Button) -> None:
        if self.robot.get_running():
            if button == Button.CENTER:
                self.robot.end_run()
        else:
            if button == Button.RIGHT:
                self.incerement_index()
            elif button == Button.LEFT:
                self.decrement_index()
            elif button == Button.CENTER:
                self.robot.execute_run(self.run_index)

    def incerement_index(self) -> None:
        if self.run_index == len(self.robot.runs) - 1:
            self.run_index = 0
        else:
            self.run_index += 1

    def decrement_index(self) -> None:
        if self.run_index == 0:
            self.run_index = len(self.robot.runs) - 1
        else:
            self.run_index -= 1


class DriveForward(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller

        self.speed = abs(speed)
        self.distance = abs(distance)

        self.current_distance = 0

    def start(self) -> None:
        self.controller.reset_drive(0)

    def check(self) -> bool:
        self.controller.run_drive_left(self.speed),
        self.controller.run_drive_right(self.speed)

        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_drive()


class DriveBackward(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = -abs(speed)
        self.distance = abs(distance)

    def start(self) -> None:
        self.controller.reset_drive(0)

    def check(self) -> bool:
        self.current_distance = self.controller.angle_drive_left()
        self.controller.run_drive_left(self.speed)
        self.controller.run_drive_right(self.speed)
        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_drive()


class ModuleLeft(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = abs(speed)
        self.distance = abs(distance)

    def start(self) -> None:
        self.controller.reset_module_left(0)

    def check(self) -> bool:
        self.current_distance = self.controller.angle_module_left()
        self.controller.run_module_left(self.speed)
        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_module_left()


class ModuleRight(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = abs(speed)
        self.distance = abs(distance)

    def start(self) -> None:
        self.controller.reset_module_right(0)

    def check(self) -> bool:
        self.current_distance = self.controller.angle_module_right()
        self.controller.run_module_right(self.speed)
        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_module_right()


class TurnLeft(Task):
    def __init__(self, controller, speed: int, angle: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = abs(speed)
        self.target = -float(abs(angle))
        self.start_target = self.controller.get_gyro_angle()

    def start(self) -> None:
        pass

    def check(self) -> bool:
        gyro_angle = self.controller.get_gyro_angle() - self.start_target
        self.controller.run_drive_left(self.speed)
        return gyro_angle <= self.target

    def stop(self) -> None:
        self.controller.brake_drive_left()


class TurnRight(Task):
    def __init__(self, controller, speed: int, angle: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = abs(speed)
        self.target = float(abs(angle))
        self.start_target = self.controller.get_gyro_angle()

    def start(self) -> None:
        pass

    def check(self) -> bool:
        gyro_angle = self.controller.get_gyro_angle() - self.start_target
        self.controller.run_drive_right(self.speed)
        return gyro_angle >= self.target

    def stop(self) -> None:
        self.controller.brake_drive_right()


class Tasks:
    def __init__(self, robot) -> None:
        self.robot = robot
        self.controller = robot.controller

    def menu(self) -> Menu:
        return Menu(self.robot)

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
