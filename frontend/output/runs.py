from robot import Robot
class Test:
	def __init__(self):
		self.run_name = 'test'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await robot.drive_backward(distance=67,speed=56)
		await robot.drive_backward(distance=67,speed=56)
		await robot.drive_forward(distance=67,speed=56)
		await robot.drive_forward(distance=67,speed=56)
		await robot.drive_backward(distance=67,speed=56)
		await robot.drive_backward(distance=67,speed=56)
		await robot.drive_forward(distance=67,speed=56)