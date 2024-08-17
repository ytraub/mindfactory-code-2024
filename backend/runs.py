"""
This is a generated file. Don't change anything manually.
"""

from robot import Robot

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.turn_left_on_spot(angle=90,speed=40),
		robot.tasks.turn_right_on_spot(angle=90,speed=40),
		robot.tasks.turn_left_on_spot(angle=90,speed=40),
		robot.tasks.turn_right_on_spot(angle=90,speed=40),
		robot.tasks.turn_left_on_spot(angle=90,speed=40),
		robot.tasks.turn_right_on_spot(angle=90,speed=40),])


class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.turn_left(angle=90,speed=40),
		robot.tasks.turn_right(angle=90,speed=40),
		robot.tasks.turn_left(angle=90,speed=40),
		robot.tasks.turn_right(angle=90,speed=40),
		robot.tasks.turn_left(angle=90,speed=40),
		robot.tasks.turn_right(angle=90,speed=40),])



__runs = [Run1(),Run2(),]