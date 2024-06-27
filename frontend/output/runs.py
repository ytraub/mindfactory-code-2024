"""
This is a generated file. Don't change anything manually.
"""

from pybricks.tools import multitask
from robot import Robot

class D:
	def __init__(self):
		self.run_name = 'd'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await robot.drive_backward(speed=60,distance=300)

class S:
	def __init__(self):
		self.run_name = 's'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await robot.drive_backward(speed=60,distance=300)

class Test2:
	def __init__(self):
		self.run_name = 'test2'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await robot.drive_backward(speed=60,distance=300)

