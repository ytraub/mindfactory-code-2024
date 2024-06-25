from robot import Robot
class Test:
	def __init__(self):
		self.run_name = 'test'
		self.run_color = 'RED'
	def execute(self, robot: Robot):
		robot.drive_backward(distance=1,speed=45)
		robot.drive_forward(distance=56,speed=89)
		robot.drive_backward(distance=89,speed=9)
		robot.drive_forward(distance=1,speed=89)
