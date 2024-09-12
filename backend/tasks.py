from pybricks.parameters import Button, Color
from umath import sqrt

## Control how much of distance from a driving block is used as accel/deaccel distance as default
# 1 means all distance (100%), 0 none (0%)
# accel will be prefered over deaccel
DEFAULT_ACCEL_DISTANCE_MULTIPLIER = 0.4
DEFAULT_DEACCEL_DISTANCE_MULTIPLIER = 0.4


## Control how fast the robot will start driving with accel on default
# Setting it to 0 will cause the robot to not drive at all
DEFAULT_START_SPEED = 10


## Defaults for pid multipliers
# Adjust as needed
DEFAULT_KP = 1
DEFAULT_KI = 0.002
DEFAULT_KD = 0.1


## Helper function for accel/deaccel
# Adjust as needed
def f(x):
    return sqrt(abs(x))


class Task:
    def __init__(self) -> None:
        self.next_tasks: Task | list[Task] | None = None

    def start(self) -> None:
        pass

    def check(self) -> bool:
        return True

    def stop(self) -> None:
        pass

    def set_next_tasks(self, tasks) -> None:
        self.next_tasks = tasks

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
            if self.robot.get_running():
                self.controller.hub.light.on(Color.BLUE)
            else:
                self.controller.hub.light.on(Color.GREEN)


        if self.run_index == 0:
            self.controller.hub.display.char("#")
        else:    
            self.controller.hub.display.char(str(self.run_index))

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

class StartRunWithColor(Task):
    def __init__(self, robot, controller) -> None:
        super().__init__()
        self.robot = robot
        self.controller = controller

    def start(self):
        module_color = self.controller.get_run_color()
        run_index = None

        for i in range(len(self.robot.runs) - 1):
            if self.robot.runs[i].run_color == str(module_color):
                run_index = i

        if run_index == None:
            print(f"No run found for color: {str(module_color)}")
            return
        
        self.robot.execute_run(run_index)

    def check(self) -> bool:
        return True

class DriveForwardGyro(Task):
    def __init__(
        self,
        controller,
        speed: int,
        distance: int,
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
        kp: int,
        ki: int,
        kd: int,
        gyro_target: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.distance = abs(distance)
        self.max_speed = abs(speed)
        self.start_speed = abs(start_speed)
        self.accel_distance = abs(accel_distance)
        self.deaccel_distance = abs(deaccel_distance)
        self.target = abs(gyro_target)

        self.kp = abs(kp)
        self.ki = abs(ki)
        self.kd = abs(kd)

        self.speed = self.start_speed
        self.current_distance = 0

        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0

    def start(self) -> None:
        self.controller.reset_drive(0)
        self.controller.reset_gyro()

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

        self.error = self.target - self.controller.get_gyro_angle()
        self.integral = self.integral + self.error
        self.derivative = self.error - self.last_error

        correction = (
            (self.kp * self.error)
            + (self.ki * self.integral)
            + (self.kd * self.derivative)
        )

        self.controller.run_drive_left(self.speed + correction)
        self.controller.run_drive_right(self.speed - correction)

        self.last_error = self.error
        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_drive()


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

        self.speed = self.start_speed
        self.current_distance = 0

        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0

    def start(self) -> None:
        self.controller.reset_drive(0)
        self.controller.reset_gyro()

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

        self.last_error = self.error
        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_drive()


class DriveForwardTimeGyro(Task):
    def __init__(
        self,
        controller,
        speed: int,
        time: int,
        kp: int,
        ki: int,
        kd: int,
        gyro_target: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.time = abs(time)
        self.speed = abs(speed)
        self.target = abs(gyro_target)

        self.kp = abs(kp)
        self.ki = abs(ki)
        self.kd = abs(kd)

        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0

        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.controller.reset_gyro()
        self.timer.start()

    def check(self) -> bool:
        self.error = self.target - self.controller.get_gyro_angle()
        self.integral = self.integral + self.error
        self.derivative = self.error - self.last_error

        correction = (
            (self.kp * self.error)
            + (self.ki * self.integral)
            + (self.kd * self.derivative)
        )

        self.controller.run_drive_left(self.speed + correction)
        self.controller.run_drive_right(self.speed - correction)

        self.last_error = self.error
        return self.timer.finished(self.time)

    def stop(self) -> None:
        self.controller.brake_drive()


class DriveBackwardGyro(Task):
    def __init__(
        self,
        controller,
        speed: int,
        distance: int,
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
        kp: int,
        ki: int,
        kd: int,
        gyro_target: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.distance = abs(distance)
        self.max_speed = abs(speed)
        self.start_speed = abs(start_speed)
        self.accel_distance = abs(accel_distance)
        self.deaccel_distance = abs(deaccel_distance)
        self.target = abs(gyro_target)

        self.kp = abs(kp)
        self.ki = abs(ki)
        self.kd = abs(kd)

        self.current_distance = 0
        self.speed = self.start_speed

        self.integral = 0
        self.derivative = 0
        self.error = 0
        self.last_error = 0

    def start(self) -> None:
        self.controller.reset_drive(0)
        self.controller.reset_gyro()

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

        self.error = self.target - self.controller.get_gyro_angle()
        self.integral = self.integral + self.error
        self.derivative = self.error - self.last_error

        correction = (
            (self.kp * self.error)
            + (self.ki * self.integral)
            + (self.kd * self.derivative)
        )

        self.controller.run_drive_left(-(self.speed - correction))
        self.controller.run_drive_right(-(self.speed + correction))

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
        self.controller.reset_gyro()

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

        self.controller.run_drive_left(-(self.speed))
        self.controller.run_drive_right(-(self.speed))

        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_drive()


class ModuleLeftCW(Task):
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


class ModuleLeftTimeCW(Task):
    def __init__(
        self,
        controller,
        speed: int,
        time: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.time = abs(time)
        self.speed = abs(speed)

        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.timer.start()

    def check(self) -> bool:
        self.controller.run_module_left(self.speed)

        return self.timer.finished(self.time)

    def stop(self) -> None:
        self.controller.brake_module_left()


class ModuleRightCW(Task):
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


class ModuleRightTimeCW(Task):
    def __init__(
        self,
        controller,
        speed: int,
        time: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.time = abs(time)
        self.speed = abs(speed)

        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.timer.start()

    def check(self) -> bool:
        self.controller.run_module_right(self.speed)

        return self.timer.finished(self.time)

    def stop(self) -> None:
        self.controller.brake_module_right()


class ModuleLeftCCW(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = -abs(speed)
        self.distance = abs(distance)

    def start(self) -> None:
        self.controller.reset_module_left(0)

    def check(self) -> bool:
        self.controller.run_module_left(self.speed)

        return abs(self.controller.angle_module_left()) >= self.distance

    def stop(self) -> None:
        self.controller.brake_module_left()


class ModuleLeftTimeCCW(Task):
    def __init__(
        self,
        controller,
        speed: int,
        time: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.time = abs(time)
        self.speed = -abs(speed)

        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.timer.start()

    def check(self) -> bool:
        self.controller.run_module_left(self.speed)

        return self.timer.finished(self.time)

    def stop(self) -> None:
        self.controller.brake_module_left()


class ModuleRightCCW(Task):
    def __init__(self, controller, speed: int, distance: int) -> None:
        super().__init__()
        self.controller = controller
        self.speed = -abs(speed)
        self.distance = abs(distance)

    def start(self) -> None:
        self.controller.reset_module_right(0)

    def check(self) -> bool:
        self.controller.run_module_right(self.speed)

        return abs(self.controller.angle_module_right()) >= self.distance

    def stop(self) -> None:
        self.controller.brake_module_right()


class ModuleRightTimeCCW(Task):
    def __init__(
        self,
        controller,
        speed: int,
        time: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.time = abs(time)
        self.speed = -abs(speed)

        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.timer.start()

    def check(self) -> bool:
        self.controller.run_module_right(self.speed)

        return self.timer.finished(self.time)

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
        self.start_target = self.controller.get_gyro_angle()

    def check(self) -> bool:
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

        if abs(self.gyro_angle) < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(self.accel_distance)
            self.speed = c * f(self.gyro_angle) + self.start_speed
        elif abs(self.gyro_angle) < abs(self.target) - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(self.deaccel_distance)
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
        self.start_target = self.controller.get_gyro_angle()

    def check(self) -> bool:
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

        if abs(self.gyro_angle) < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(self.accel_distance)
            self.speed = c * f(self.gyro_angle) + self.start_speed
        elif abs(self.gyro_angle) < abs(self.target) - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(self.deaccel_distance)
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
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
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
        self.start_target = self.controller.get_gyro_angle()

    def check(self) -> bool:
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

        if abs(self.gyro_angle) < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(self.accel_distance)
            self.speed = c * f(self.gyro_angle) + self.start_speed
        elif abs(self.gyro_angle) < abs(self.target) - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(self.deaccel_distance)
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
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
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
        self.start_target = self.controller.get_gyro_angle()

    def check(self) -> bool:
        self.gyro_angle = self.controller.get_gyro_angle() - self.start_target

        if abs(self.gyro_angle) < self.accel_distance:
            c = (self.max_speed - self.start_speed) / f(self.accel_distance)
            self.speed = c * f(self.gyro_angle) + self.start_speed
        elif abs(self.gyro_angle) < abs(self.target) - self.deaccel_distance:
            self.speed = self.max_speed
        else:
            try:
                c = (self.max_speed - self.start_speed) / f(self.deaccel_distance)
                self.speed = c * f(self.distance - self.gyro_angle) + self.start_speed
            except:
                self.speed = self.start_speed

        self.controller.run_drive_left(self.speed)
        self.controller.run_drive_right(-self.speed)

        return self.gyro_angle >= self.target

    def stop(self) -> None:
        self.controller.brake_drive_left()
        self.controller.brake_drive_right()
        


class Tasks:
    def __init__(self, robot, controller) -> None:
        self.robot = robot
        self.controller = controller

    def menu(self) -> Menu:
        return Menu(self.robot, self.controller)
    
    def start_run_with_color(self) -> StartRunWithColor:
        return StartRunWithColor(self.robot, self.controller)

    def drive_forward_gyro(
        self,
        speed: int,
        distance: int,
        start_speed: int = DEFAULT_START_SPEED,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
        kp: int = DEFAULT_KP,
        ki: int = DEFAULT_KI,
        kd: int = DEFAULT_KD,
    ) -> DriveForwardGyro:
        if accel_distance < 0:
            accel_distance = distance * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = distance * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return DriveForwardGyro(
            self.controller,
            speed=speed,
            distance=distance,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
            kp=kp,
            ki=ki,
            kd=kd,
            gyro_target=0,
        )

    def drive_forward(
        self,
        speed: int,
        distance: int,
        start_speed: int = DEFAULT_START_SPEED,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> DriveForwardGyro:
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

    def drive_forward_time_gyro(
        self,
        speed: int,
        time: int,
        kp: int = DEFAULT_KP,
        ki: int = DEFAULT_KI,
        kd: int = DEFAULT_KD,
    ) -> DriveForwardTimeGyro:

        return DriveForwardTimeGyro(
            self.controller,
            speed=speed,
            time=time,
            kp=kp,
            ki=ki,
            kd=kd,
            gyro_target=0,
        )

    def drive_backward_gyro(
        self,
        speed: int,
        distance: int,
        start_speed: int = DEFAULT_START_SPEED,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
        kp: int = DEFAULT_KP,
        ki: int = DEFAULT_KI,
        kd: int = DEFAULT_KD,
    ) -> DriveBackwardGyro:
        if accel_distance < 0:
            accel_distance = distance * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = distance * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return DriveBackwardGyro(
            self.controller,
            speed=speed,
            distance=distance,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
            kp=kp,
            ki=ki,
            kd=kd,
            gyro_target=0,
        )

    def drive_backward(
        self,
        speed: int,
        distance: int,
        start_speed: int = DEFAULT_START_SPEED,
        accel_distance: int = -1,
        deaccel_distance: int = -1,
    ) -> DriveBackwardGyro:
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

    def module_left_cw(self, speed: int, distance: int) -> ModuleLeftCW:
        return ModuleLeftCW(self.controller, speed=speed, distance=distance)
    
    def module_left_time_cw(
        self,
        speed: int,
        time: int,
    ) -> ModuleLeftTimeCW:

        return ModuleLeftTimeCW(
            self.controller,
            speed=speed,
            time=time,
        )

    def module_right_cw(self, speed: int, distance: int) -> ModuleRightCW:
        return ModuleRightCW(self.controller, speed=speed, distance=distance)

    def module_right_time_cw(
        self,
        speed: int,
        time: int,
    ) -> ModuleRightTimeCW:

        return ModuleRightTimeCW(
            self.controller,
            speed=speed,
            time=time,
        )

    def module_left_ccw(self, speed: int, distance: int) -> ModuleLeftCCW:
        return ModuleLeftCCW(self.controller, speed=speed, distance=distance)
    
    def module_left_time_ccw(
        self,
        speed: int,
        time: int,
    ) -> ModuleLeftTimeCCW:

        return ModuleLeftTimeCCW(
            self.controller,
            speed=speed,
            time=time,
        )

    def module_right_ccw(self, speed: int, distance: int) -> ModuleRightCCW:
        return ModuleRightCCW(self.controller, speed=speed, distance=distance)

    def module_right_time_ccw(
        self,
        speed: int,
        time: int,
    ) -> ModuleRightTimeCCW:

        return ModuleRightTimeCCW(
            self.controller,
            speed=speed,
            time=time,
        )


    def turn_left(
        self,
        speed: int,
        angle: int,
        start_speed: int = DEFAULT_START_SPEED,
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
        start_speed: int = DEFAULT_START_SPEED,
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
        start_speed: int = DEFAULT_START_SPEED,
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
        start_speed: int = DEFAULT_START_SPEED,
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
