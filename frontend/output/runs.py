from robot import Robot
class Test:
	def __init__(self):
		self.run_name = 'test'
		self.run_color = 'RED'
	async def execute(self, robot: Robot):
		await multitask(robot.drive_backward(distance=67,speed=56),robot.drive_forward(distance=67,speed=56),robot.drive_forward(distance=67,speed=56),robot.drive_backward(distance=67,speed=56))
		await robot.drive_forward(distance=1,speed=1)
		await robot.drive_forward(distance=1,speed=1)