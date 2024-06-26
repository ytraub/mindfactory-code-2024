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
		await robot.drive_forward(distance=1000,speed=20)