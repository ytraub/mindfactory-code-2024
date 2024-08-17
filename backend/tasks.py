from pybricks.parameters import Button, Color

from umath import sqrt

## Control how much of distance from a driving block is used as accel/deaccel distance as default
# 1 means all distance (100%), 0 none (0%)
# accel will be prefered over deaccel
DEFAULT_ACCEL_DISTANCE_MULTIPLIER = 0.4
DEFAULT_DEACCEL_DISTANCE_MULTIPLIER = 0.4


## Helper function for accel/deaccel
# Can be adjusted as needed
def f(x):
    return sqrt(x)


class Task:
    def __init__(self) -> None:
        self.next_tasks = []

    def start(self) -> None:
        pass

    def check(self) -> bool:
        return True

    def stop(self) -> None:
        pass

    def add_next_tasks(self, tasks) -> None:
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
        if not self.controller.hub.imu.ready() or self.robot.get_loading():
            self.controller.hub.light.on(Color.RED)
        else:
            if self.robot.running:
                self.controller.hub.light.on(Color.BLUE)
            else:
                self.controller.hub.light.on(Color.GREEN)

        self.controller.hub.display.char(str(self.run_index + 1))

        buttons = self.controller.get_buttons()
        if len(buttons) == 1:
            self.handle_button(list(buttons)[0])

        return False

    def handle_button(self, button: Button) -> None:
        while len(self.controller.get_buttons()):
            continue

        if self.robot.get_running():
            if button == Button.CENTER:
                self.robot.interrupt_run()
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
    def __init__(
        self,
        controller,
        speed: int,
        distance: int,
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.distance = abs(distance)
        self.max_speed = abs(speed)
        self.start_speed = abs(start_speed)
        self.accel_distance = abs(accel_distance)
        self.deaccel_distance = abs(deaccel_distance)

        self.current_distance = 0
        self.speed = self.start_speed

    def start(self) -> None:
        self.controller.reset_drive(0)

    def check(self) -> bool:
        self.current_distance = abs(self.controller.angle_drive_left())

        if self.current_distance < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(self.accel_distance)
            self.speed = c * f(self.current_distance) + self.start_speed
        elif self.current_distance < self.distance - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            c = (self.max_speed - self.start_speed) / f(self.deaccel_distance)
            self.speed = c * f(self.distance - self.current_distance) + self.start_speed

        self.controller.run_drive_left(self.speed)
        self.controller.run_drive_right(self.speed)

        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_drive()


class DriveBackward(Task):
    def __init__(
        self,
        controller,
        speed: int,
        distance: int,
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.distance = abs(distance)
        self.max_speed = abs(speed)
        self.start_speed = abs(start_speed)
        self.accel_distance = abs(accel_distance)
        self.deaccel_distance = abs(deaccel_distance)

        self.current_distance = 0
        self.speed = self.start_speed

    def start(self) -> None:
        self.controller.reset_drive(0)

    def check(self) -> bool:
        self.current_distance = abs(self.controller.angle_drive_left())

        if self.current_distance < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(self.accel_distance)
            self.speed = c * f(self.current_distance) + self.start_speed
        elif self.current_distance < self.distance - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(self.deaccel_distance)
                self.speed = (
                    c * f(self.distance - self.current_distance) + self.start_speed
                )
            except:
                self.speed = self.start_speed

        self.controller.run_drive_left(-self.speed)
        self.controller.run_drive_right(-self.speed)

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
        self.controller.run_module_left(self.speed)

        return self.controller.angle_module_left() >= self.distance

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
        self.controller.run_module_right(self.speed)

        return self.controller.angle_module_right() >= self.distance

    def stop(self) -> None:
        self.controller.brake_module_right()


class TurnLeft(Task):
    def __init__(
        self,
        controller,
        speed: int,
        angle: int,
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.max_speed = abs(speed)
        self.target = -float(abs(angle))
        self.start_target = self.controller.get_gyro_angle()

        self.start_speed = abs(start_speed)
        self.accel_distance = float(abs(accel_distance))
        self.deaccel_distance = float(abs(deaccel_distance))

        self.speed = start_speed
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

    def start(self) -> None:
        self.controller.reset_gyro()

    def check(self) -> bool:
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

        if abs(self.gyro_angle) < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(abs(self.accel_distance))
            self.speed = c * f(abs(self.gyro_angle)) + self.start_speed
        elif abs(self.gyro_angle) < abs(self.target) - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(abs(self.deaccel_distance))
                self.speed = c * f(self.distance - self.gyro_angle) + self.start_speed
            except:
                self.speed = self.start_speed

        self.controller.run_drive_right(self.speed)

        return self.gyro_angle <= self.target

    def stop(self) -> None:
        self.controller.brake_drive_right()


class TurnLeftOnSpot(Task):
    def __init__(
        self,
        controller,
        speed: int,
        angle: int,
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.max_speed = abs(speed)
        self.target = -float(abs(angle))
        self.start_target = self.controller.get_gyro_angle()

        self.start_speed = abs(start_speed)
        self.accel_distance = float(abs(accel_distance))
        self.deaccel_distance = float(abs(deaccel_distance))

        self.speed = start_speed
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

    def start(self) -> None:
        self.controller.reset_gyro()

    def check(self) -> bool:
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

        if abs(self.gyro_angle) < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(abs(self.accel_distance))
            self.speed = c * f(abs(self.gyro_angle)) + self.start_speed
        elif abs(self.gyro_angle) < abs(self.target) - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(abs(self.deaccel_distance))
                self.speed = c * f(self.distance - self.gyro_angle) + self.start_speed
            except:
                self.speed = self.start_speed

        self.controller.run_drive_right(self.speed)
        self.controller.run_drive_left(-self.speed)

        return self.gyro_angle <= self.target

    def stop(self) -> None:
        self.controller.brake_drive_right()


class TurnRight(Task):
    def __init__(
        self,
        controller,
        speed: int,
        angle: int,
        start_speed: int = 10,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.max_speed = abs(speed)
        self.target = float(abs(angle))
        self.start_target = self.controller.get_gyro_angle()

        self.start_speed = abs(start_speed)
        self.accel_distance = float(abs(accel_distance))
        self.deaccel_distance = float(abs(deaccel_distance))

        self.speed = start_speed
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

    def start(self) -> None:
        self.controller.reset_gyro()

    def check(self) -> bool:
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

        if abs(self.gyro_angle) < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(abs(self.accel_distance))
            self.speed = c * f(abs(self.gyro_angle)) + self.start_speed
        elif abs(self.gyro_angle) < abs(self.target) - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(abs(self.deaccel_distance))
                self.speed = c * f(self.distance - self.gyro_angle) + self.start_speed
            except:
                self.speed = self.start_speed

        self.controller.run_drive_left(self.speed)

        return self.gyro_angle >= self.target

    def stop(self) -> None:
        self.controller.brake_drive_left()


class TurnRightOnSpot(Task):
    def __init__(
        self,
        controller,
        speed: int,
        angle: int,
        start_speed: int = 10,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.max_speed = abs(speed)
        self.target = float(abs(angle))
        self.start_target = self.controller.get_gyro_angle()

        self.start_speed = abs(start_speed)
        self.accel_distance = float(abs(accel_distance))
        self.deaccel_distance = float(abs(deaccel_distance))

        self.speed = start_speed
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

    def start(self) -> None:
        self.controller.reset_gyro()

    def check(self) -> bool:
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

        if abs(self.gyro_angle) < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(abs(self.accel_distance))
            self.speed = c * f(abs(self.gyro_angle)) + self.start_speed
        elif abs(self.gyro_angle) < abs(self.target) - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(abs(self.deaccel_distance))
                self.speed = c * f(self.distance - self.gyro_angle) + self.start_speed
            except:
                self.speed = self.start_speed

        self.controller.run_drive_left(self.speed)
        self.controller.run_drive_right(-self.speed)

        return self.gyro_angle >= self.target

    def stop(self) -> None:
        print(self.controller.get_gyro_raw_angle())
        self.controller.brake_drive_left()
        self.controller.brake_drive_right()


class Tasks:
    def __init__(self, robot, controller) -> None:
        self.robot = robot
        self.controller = controller

    def menu(self) -> Menu:
        return Menu(self.robot, self.controller)

    def drive_forward(
        self,
        speed: int,
        distance: int,
        start_speed: int = 10,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> DriveForward:
        if accel_distance < 0:
            accel_distance = distance * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = distance * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return DriveForward(
            self.controller,
            speed=speed,
            distance=distance,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
        )

    def drive_backward(
        self,
        speed: int,
        distance: int,
        start_speed: int = 10,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> DriveBackward:
        if accel_distance < 0:
            accel_distance = distance * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = distance * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return DriveBackward(
            self.controller,
            speed=speed,
            distance=distance,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
        )

    def module_left(self, speed: int, distance: int) -> ModuleLeft:
        return ModuleLeft(self.controller, speed=speed, distance=distance)

    def module_right(self, speed: int, distance: int) -> ModuleRight:
        return ModuleRight(self.controller, speed=speed, distance=distance)

    def turn_left(
        self,
        speed: int,
        angle: int,
        start_speed: int = 10,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> TurnLeft:
        if accel_distance < 0:
            accel_distance = angle * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = angle * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return TurnLeft(
            self.controller,
            speed=speed,
            angle=angle,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
        )

    def turn_left_on_spot(
        self,
        speed: int,
        angle: int,
        start_speed: int = 10,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> TurnLeftOnSpot:
        if accel_distance < 0:
            accel_distance = angle * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = angle * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return TurnLeftOnSpot(
            self.controller,
            speed=speed,
            angle=angle,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
        )

    def turn_right(
        self,
        speed: int,
        angle: int,
        start_speed: int = 10,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> TurnRight:
        if accel_distance < 0:
            accel_distance = angle * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = angle * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return TurnRight(
            self.controller,
            speed=speed,
            angle=angle,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
        )

    def turn_right_on_spot(
        self,
        speed: int,
        angle: int,
        start_speed: int = 10,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> TurnRightOnSpot:
        if accel_distance < 0:
            accel_distance = angle * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = angle * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return TurnRightOnSpot(
            self.controller,
            speed=speed,
            angle=angle,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
        )
