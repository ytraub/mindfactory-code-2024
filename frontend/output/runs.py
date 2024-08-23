"""
This is a generated file. Don't change anything manually.
"""

from robot import Robot

class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.turn_left_on_spot(angle=90,speed=40),
		robot.tasks.turn_right_on_spot(angle=90,speed=40),
		robot.tasks.turn_left_on_spot(angle=90,speed=40),
		robot.tasks.turn_right_on_spot(angle=90,speed=40),
		robot.tasks.turn_left_on_spot(angle=90,speed=40),
		robot.tasks.turn_right_on_spot(angle=90,speed=40),])


class Run3:
	def __init__(self):
		self.run_name = 'run3'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.drive_backward(speed=40,distance=1000),])


class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.drive_forward(speed=40,distance=1000),])



__runs = [Run2(),Run3(),Run1(),]