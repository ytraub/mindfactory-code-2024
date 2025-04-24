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


## Default time in ms the align block spends adjusting according to the global error
# Adjust as needed
DEFAULT_ALIGN_TIME = 1000

# before alex and casi changes
# DEFAULT_KP = 1
# DEFAULT_KI = 0.002
# DEFAULT_KD = 0.1


## Helpers
# Error printing
def print_runtime_error(*args) -> None:
    print("[RUNTIME ERROR]: ", *args)


# Helper function for accel/deaccel
# Adjust as needed
def f(x):
    return sqrt(abs(x))

# Helper to wait in a block
# Blocks the entire event loop
def wait(controller, time: int) -> None:
    timer = controller.create_timer()
    timer.start()

    while not timer.finished(time):
        pass

    return

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


class Drive(Task):
    def __init__(
        self,
        controller,
        forward: bool,
        speed: int,
        distance: int,
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.forward = forward

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

        if self.forward:
            self.controller.run_drive_left(self.speed)
            self.controller.run_drive_right(self.speed)
        else:
            self.controller.run_drive_left(-self.speed)
            self.controller.run_drive_right(-self.speed)

        self.last_error = self.error
        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_drive()


class DriveGyro(Task):
    def __init__(
        self,
        controller,
        forward: bool,
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

        self.forward = forward

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

        global_error = self.controller.get_global_error()
        self.target = 0 + global_error

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

        if self.forward:
            self.controller.run_drive_left(self.speed + correction)
            self.controller.run_drive_right(self.speed - correction)
            # print(self.speed + correction, self.speed - correction)
        else:
            self.controller.run_drive_left(-(self.speed - correction))
            self.controller.run_drive_right(-(self.speed + correction))

        self.last_error = self.error
        return self.current_distance >= self.distance

    def stop(self) -> None:
        self.controller.brake_drive()


class DriveTimeGyro(Task):
    def __init__(
        self,
        controller,
        forward: bool,
        speed: int,
        time: int,
        kp: int,
        ki: int,
        kd: int,
        gyro_target: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.forward = forward

        self.time = abs(time)
        self.speed = abs(speed)
        self.target = abs(gyro_target) - self.controller.get_global_error()

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

        if self.forward:
            self.controller.run_drive_left(self.speed + correction)
            self.controller.run_drive_right(self.speed - correction)
        else:
            self.controller.run_drive_left(-(self.speed - correction))
            self.controller.run_drive_right(-(self.speed + correction))

        self.last_error = self.error
        return self.timer.finished(self.time)

    def stop(self) -> None:
        self.controller.brake_drive()


class Module(Task):
    def __init__(
        self, controller, left: bool, cw: bool, speed: int, distance: int
    ) -> None:
        super().__init__()
        self.controller = controller
        self.left = left
        self.cw = cw

        self.distance = abs(distance)
        if cw:
            self.speed = abs(speed)
        else:
            self.speed = -abs(speed)

    def start(self) -> None:
        if self.left:
            self.controller.reset_module_left(0)
        else:
            self.controller.reset_module_right(0)
            

    def check(self) -> bool:
        if self.left:
            self.controller.run_module_left(self.speed)
            return abs(self.controller.angle_module_left()) >= self.distance
        else:
            self.controller.run_module_right(self.speed)
            return abs(self.controller.angle_module_right()) >= self.distance

    def stop(self) -> None:
        if self.left:
            self.controller.brake_module_left()
        else:
            self.controller.brake_module_right()


class ModuleTime(Task):
    def __init__(
        self,
        controller,
        left: bool,
        cw: bool,
        speed: int,
        time: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.left = left
        self.cw = cw

        self.time = abs(time)
        if cw:
            self.speed = abs(speed)
        else:
            self.speed = -abs(speed)

        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.timer.start()

    def check(self) -> bool:
        if self.left:
            self.controller.run_module_left(self.speed)
        else:
            self.controller.run_module_right(self.speed)

        return self.timer.finished(self.time)

    def stop(self) -> None:
        if self.left:
            self.controller.brake_module_left()
        else:
            self.controller.brake_module_right()

class DriveCustom(Task):
    def __init__(
        self,
        controller,
        forward: bool,
        speed_left: int,
        speed_right: int,
        time: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.forward = forward

        self.time = abs(time)
        self.speed_left = abs(speed_left)
        self.speed_right = abs(speed_right)

        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.timer.start()

    def check(self) -> bool:
        if self.forward:
            self.controller.run_drive_left(self.speed_left)
            self.controller.run_drive_right(self.speed_right)
        else:
            self.controller.run_drive_left(-self.speed_left)
            self.controller.run_drive_right(-self.speed_right)

        return self.timer.finished(self.time)

    def stop(self) -> None:
        self.controller.brake_drive()

class Turn(Task):
    def __init__(
        self,
        controller,
        left: bool,
        on_spot: bool,
        speed: int,
        angle: int,
        start_speed: int,
        accel_distance: int,
        deaccel_distance: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.left = left
        self.on_spot = on_spot

        self.max_speed = abs(speed)
        self.start_speed = abs(start_speed)
        self.speed = start_speed

        self.target = float(abs(angle))
        self.accel_distance = float(abs(accel_distance))
        self.deaccel_distance = float(abs(deaccel_distance))

        self.start_target = 0
        self.gyro_angle = 0

    def start(self) -> None:
        self.controller.reset_gyro()
        self.start_target = self.controller.get_gyro_angle()

        if self.left:
            self.controller.desired_target -= self.target
        else:
            self.controller.desired_target += self.target

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
                self.speed = (
                    c * f(self.target - abs(self.gyro_angle)) + self.start_speed
                )
            except:
                self.speed = self.start_speed

        if self.left:
            if self.on_spot:
                self.controller.run_drive_right(self.speed)
                self.controller.run_drive_left(-self.speed)
            else:
                self.controller.run_drive_right(self.speed)
        else:
            if self.on_spot:
                self.controller.run_drive_right(-self.speed)
                self.controller.run_drive_left(self.speed)
            else:
                self.controller.run_drive_left(self.speed)

        return abs(self.gyro_angle) >= self.target

    def stop(self) -> None:
        self.controller.brake_drive()


class AlignGyro(Task):
    def __init__(
        self,
        controller,
        time: int,
        kp: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        
        self.kp = kp

        self.time = time
        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.controller.reset_gyro()
        self.timer.start()

        global_error = self.controller.get_global_error()
        self.target = 0 + global_error

    def check(self) -> bool:
        error = self.target - self.controller.get_gyro_angle()
        correction = self.kp * error
        
        self.controller.run_drive_left(correction)
        self.controller.run_drive_right(-correction)

        return self.timer.finished(self.time)

    def stop(self) -> None:
        self.controller.brake_drive()


class Menu(Task):
    def __init__(self, robot, controller) -> None:
        super().__init__()
        self.robot = robot
        self.controller = controller

        self.run_index = 0
        print(robot.controller.hub.battery.voltage())

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

        for i, run in enumerate(self.robot.runs):
            if not str(run.run_color) == str(module_color):
                continue

            run_index = i
            break

        if run_index == None:
            print(f"No run found for color: {str(module_color)}")
            return

        self.robot.execute_run(run_index)


class SetEvent(Task):
    def __init__(self, robot, event_index: str) -> None:
        super().__init__()
        self.runtime = robot.runtime
        self.event_index = event_index

    def start(self) -> None:
        self.runtime.add_untriggered_events(self.event_index)


class TriggerEvent(Task):
    def __init__(self, robot, event_index: str) -> None:
        super().__init__()
        self.runtime = robot.runtime
        self.event_index = event_index

    def start(self) -> None:
        self.runtime.trigger_event(self.event_index)


class WaitEvent(Task):
    def __init__(self, robot, event_index: str) -> None:
        super().__init__()
        self.runtime = robot.runtime
        self.event_index = event_index

    def check(self) -> bool:
        return not self.runtime.check_untriggered_event(self.event_index)


class WaitMs(Task):
    def __init__(
        self,
        controller,
        time: int,
    ) -> None:
        super().__init__()
        self.controller = controller

        self.time = abs(time)

        self.timer = self.controller.create_timer()

    def start(self) -> None:
        self.timer.start()

    def check(self) -> bool:
        return self.timer.finished(self.time)


class CreateGlobalTimer(Task):
    def __init__(
        self,
        robot,
        controller,
        index: int,
    ) -> None:
        super().__init__()
        self.controller = controller
        self.robot = robot

        self.index = index

    def start(self) -> None:
        timer = self.controller.create_timer()
        timer.start()

        self.robot.timers[str(self.index)] = timer

    def check(self) -> None:
        return True


class WaitGlobalTimer(Task):
    def __init__(
        self,
        robot,
        index: int,
        time: int,
    ) -> None:
        super().__init__()
        self.robot = robot

        self.index = index
        self.time = time
        self.timer = None

    def start(self) -> None:
        if self.robot.timers.get(str(self.index)):
            self.timer = self.robot.timers[str(self.index)]
        else:
            print_runtime_error(f"No timer with index: {self.index} found")

    def check(self) -> None:
        if self.timer:
            return self.timer.reached(self.time)
        else:
            print("No timer found for index", self.index)
            return True

class Tasks:
    def __init__(self, robot, controller) -> None:
        self.robot = robot
        self.controller = controller

    def menu(self) -> Menu:
        return Menu(self.robot, self.controller)

    def start_run_with_color(self) -> StartRunWithColor:
        return StartRunWithColor(self.robot, self.controller)

    def set_event(self, index: str) -> SetEvent:
        return SetEvent(self.robot, event_index=index)

    def trigger_event(self, index: str) -> TriggerEvent:
        return TriggerEvent(self.robot, event_index=index)

    def wait_event(self, index: str) -> WaitEvent:
        return WaitEvent(self.robot, event_index=index)

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
    ) -> DriveGyro:
        if accel_distance < 0:
            accel_distance = distance * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = distance * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return DriveGyro(
            self.controller,
            forward=True,
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
    ) -> Drive:
        if accel_distance < 0:
            accel_distance = distance * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = distance * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return Drive(
            self.controller,
            forward=True,
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
    ) -> DriveTimeGyro:

        return DriveTimeGyro(
            self.controller,
            forward=True,
            speed=speed,
            time=time,
            kp=kp,
            ki=ki,
            kd=kd,
            gyro_target=0,
        )

    def drive_backward_time_gyro(
        self,
        speed: int,
        time: int,
        kp: int = DEFAULT_KP,
        ki: int = DEFAULT_KI,
        kd: int = DEFAULT_KD,
    ) -> DriveTimeGyro:

        return DriveTimeGyro(
            self.controller,
            forward=False,
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
    ) -> DriveGyro:
        if accel_distance < 0:
            accel_distance = distance * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = distance * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return DriveGyro(
            self.controller,
            forward=False,
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
    ) -> Drive:
        if accel_distance < 0:
            accel_distance = distance * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = distance * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return Drive(
            self.controller,
            forward=False,
            speed=speed,
            distance=distance,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
        )
    
    def drive_custom_forward(self, time: int, speed_left: int, speed_right: int) -> DriveCustom:
        return DriveCustom(self.controller, forward=True, speed_left=speed_left, speed_right=speed_right, time=time)
        
    def drive_custom_backward(self, time: int, speed_left: int, speed_right: int) -> DriveCustom:
        return DriveCustom(self.controller, forward=False, speed_left=speed_left, speed_right=speed_right, time=time)
        

    def align_gyro(self, time: int = DEFAULT_ALIGN_TIME, kp: int = DEFAULT_KP) -> AlignGyro:
        return AlignGyro(self.controller, time=time, kp=kp)

    def module_left_cw(self, speed: int, distance: int) -> Module:
        return Module(
            self.controller, left=True, cw=True, speed=speed, distance=distance
        )

    def module_left_time_cw(
        self,
        speed: int,
        time: int,
    ) -> Module:

        return ModuleTime(
            self.controller,
            left=True,
            cw=True,
            speed=speed,
            time=time,
        )

    def module_right_cw(self, speed: int, distance: int) -> Module:
        return Module(
            self.controller, left=False, cw=True, speed=speed, distance=distance
        )

    def module_right_time_cw(
        self,
        speed: int,
        time: int,
    ) -> ModuleTime:

        return ModuleTime(
            self.controller,
            left=False,
            cw=True,
            speed=speed,
            time=time,
        )

    def module_left_ccw(self, speed: int, distance: int) -> Module:
        return Module(
            self.controller, left=True, cw=False, speed=speed, distance=distance
        )

    def module_left_time_ccw(
        self,
        speed: int,
        time: int,
    ) -> ModuleTime:

        return ModuleTime(
            self.controller,
            left=True,
            cw=False,
            speed=speed,
            time=time,
        )

    def module_right_ccw(self, speed: int, distance: int) -> Module:
        return Module(
            self.controller, left=False, cw=False, speed=speed, distance=distance
        )

    def module_right_time_ccw(
        self,
        speed: int,
        time: int,
    ) -> ModuleTime:

        return ModuleTime(
            self.controller,
            left=False,
            cw=False,
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
    ) -> Turn:
        if accel_distance < 0:
            accel_distance = angle * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = angle * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return Turn(
            self.controller,
            left=True,
            on_spot=False,
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
    ) -> Turn:
        if accel_distance < 0:
            accel_distance = angle * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = angle * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return Turn(
            self.controller,
            left=True,
            on_spot=True,
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
    ) -> Turn:
        if accel_distance < 0:
            accel_distance = angle * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = angle * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return Turn(
            self.controller,
            left=False,
            on_spot=False,
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
    ) -> Turn:
        if accel_distance < 0:
            accel_distance = angle * DEFAULT_ACCEL_DISTANCE_MULTIPLIER

        if deaccel_distance < 0:
            deaccel_distance = angle * DEFAULT_DEACCEL_DISTANCE_MULTIPLIER

        return Turn(
            self.controller,
            left=False,
            on_spot=True,
            speed=speed,
            angle=angle,
            start_speed=start_speed,
            accel_distance=accel_distance,
            deaccel_distance=deaccel_distance,
        )

    def wait_ms(self, time: int ) -> WaitMs:
        return WaitMs(self.controller, time=time)

    def create_global_timer(self, index: int) -> CreateGlobalTimer:
        return CreateGlobalTimer(self.robot, self.controller, index=index)

    def wait_global_timer(self, index: int, time: int) -> WaitGlobalTimer:
        return WaitGlobalTimer(self.robot, index=index, time=time)
