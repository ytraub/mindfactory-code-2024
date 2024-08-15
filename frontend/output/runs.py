"""
This is a generated file. Don't change anything manually.
"""

from robot import Robot

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.turn_left(speed=20,angle=90),
		robot.tasks.turn_right(angle=90,speed=20),])



__runs = [Run1(),]