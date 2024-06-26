"""
This is an generated file. Don't change anything manually.
"""
from pybricks.tools import multitask
from robot import Robot
class Test:
	def __init__(self):
		self.run_name = 'test'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await robot.drive_forward(distance=200,speed=20)
		await robot.module_right(distance=1000,speed=20)
		await multitask(robot.module_left(distance=1000,speed=50),robot.drive_forward(distance=1000,speed=20))
		await robot.drive_backward(speed=60,distance=300)