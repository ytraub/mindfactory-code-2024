"""
This is a generated file. Don't change anything manually.
"""

from robot import Robot

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'Color.BLUE'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.module_left_time_cw(time=200,speed=100),
		robot.tasks.drive_forward_gyro(speed=40,distance=200),
		robot.tasks.turn_left_on_spot(angle=50,speed=30),
		robot.tasks.drive_forward_gyro(speed=40,distance=200),
		robot.tasks.module_left_ccw(distance=300,speed=80),
		robot.tasks.drive_forward_time_gyro(time=500,speed=50),], self.run_color)


class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'Color.RED'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.turn_right(angle=360,speed=40),], self.run_color)


class Run3:
	def __init__(self):
		self.run_name = 'run3'
		self.run_color = 'Color.GREEN'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.drive_backward(speed=40,distance=1000),], self.run_color)



__runs = [Run1(),Run2(),Run3(),]