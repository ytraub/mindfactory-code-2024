"""
This is a generated file. Don't change anything manually.
"""

from robot import Robot

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.turn_left(speed=90,angle=50),
		robot.tasks.turn_right(angle=90,speed=50),])


class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.drive_forward(speed=100,distance=1000),])


class Run3:
	def __init__(self):
		self.run_name = 'run3'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.module_right(speed=60,distance=500),
		[robot.tasks.module_left(speed=60,distance=500),robot.tasks.drive_forward(speed=100,distance=300)],
		robot.tasks.drive_forward(speed=100,distance=500),
		robot.tasks.drive_backward(distance=240,speed=45),])



__runs = [Run1(),Run2(),Run3(),]