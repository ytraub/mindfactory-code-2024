from robot import Robot
class Test:
	def __init__(self):
		self.run_name = 'test'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await robot.drive_forward(distance=100,speed=10)
		await robot.drive_backward(speed=56,distance=670)
		await robot.module_left(speed=100,distance=500)