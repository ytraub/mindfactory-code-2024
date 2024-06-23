import robot
class Test:
	def __init__(self):
		self.run_name = 'test'
		self.run_color = 'RED'
	def execute(self):
		robot.drive_forward(speed=100,distance=1000)
