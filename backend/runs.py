"""
This is a generated file. Don't change anything manually.
"""

from robot import Robot

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.drive_forward(distance=500,speed=60,accel_distance=500,deaccel_distance=0),])



__runs = [Run1(),]