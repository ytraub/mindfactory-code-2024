from pybricks.tools import run_task
from robot import Robot

robot = Robot()
run_task(robot.run_drive_target_forward(40, 2000))
