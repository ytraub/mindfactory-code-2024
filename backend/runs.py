"""
This is a generated file. Don't change anything manually.
"""

from pybricks.tools import multitask
from robot import Robot

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await robot.drive_forward(speed=100,distance=100)
		await robot.drive_backward(distance=500,speed=30)
		await multitask(robot.drive_forward(speed=100,distance=300),robot.module_left(speed=60,distance=200))

class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await robot.drive_forward(speed=100,distance=400)
		await multitask(robot.drive_forward(speed=100,distance=300),robot.module_left(speed=60,distance=200))
		await robot.drive_backward(distance=100,speed=30)

class Run3:
	def __init__(self):
		self.run_name = 'run3'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await multitask(robot.drive_forward(speed=100,distance=300),robot.module_left(speed=60,distance=500))
		await robot.drive_forward(speed=100,distance=140)
		await robot.drive_backward(distance=240,speed=45)


runs = [
	Run1(),
	Run2(),
	Run3(),
]