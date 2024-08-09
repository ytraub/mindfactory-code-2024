"""
This is a generated file. Don't change anything manually.
"""

from robot import Robot


class Run1:
    def __init__(self):
        self.run_name = "run1"
        self.run_color = "RED"

    def create_chain(self, robot: Robot):
        robot.chain(
            [
                robot.tasks.drive_forward(speed=100, distance=400),
                robot.tasks.module_right(speed=60, distance=500),
            ]
        )


__runs = [Run1()]
