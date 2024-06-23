import robot
class Test:
	def __init__(self):
		self.run_name = 'test'
		self.run_color = 'RED'
	def execute(self):
		robot.drive_backward(distance=100,speed=99)
