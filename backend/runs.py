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
		robot.tasks.drive_forward_gyro(distance=160,speed=20),
		robot.tasks.turn_left_on_spot(angle=45,speed=30),
		robot.tasks.drive_forward_gyro(distance=350,speed=40),
		robot.tasks.module_left_ccw(distance=180,speed=20),
		robot.tasks.drive_forward_gyro(distance=350,speed=40),
		robot.tasks.drive_forward_time_gyro(time=500,speed=20),
		robot.tasks.drive_backward(distance=320,speed=30),
		robot.tasks.turn_right_on_spot(angle=45,speed=30),
		robot.tasks.module_left_cw(distance=80,speed=20),
		robot.tasks.drive_forward_gyro(distance=480,speed=40),
		robot.tasks.module_left_ccw(distance=20,speed=20),
		robot.tasks.drive_forward_gyro(distance=100,speed=40),
		robot.tasks.module_left_time_cw(time=300,speed=40),], self.run_color)


class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'Color.RED'
	def create_chain(self, robot: Robot):			robot.chain([
		[robot.tasks.module_left_cw(distance=500,speed=20)],
		robot.tasks.drive_forward_gyro(speed=20,distance=500),], self.run_color)


class Run3:
	def __init__(self):
		self.run_name = 'run3'
		self.run_color = 'Color.GREEN'
	def create_chain(self, robot: Robot):			robot.chain([
		robot.tasks.drive_backward(speed=40,distance=1000),], self.run_color)



__runs = [Run1(),Run2(),Run3(),]