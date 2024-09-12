"""This is a generated file. Don't change anything manually."""

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'BLUE'
	def create_chain(self, robot):
		robot.chain([[robot.tasks.module_left_cw(distance=4,speed=20,)],
		[robot.tasks.module_left_cw(distance=1,speed=20,)],
		[robot.tasks.module_left_cw(distance=1,speed=20,)],], [1], self.run_color)
class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'RED'
	def create_chain(self, robot):
		robot.chain([[robot.tasks.module_left_cw(distance=4,speed=20,)],
		[robot.tasks.module_left_cw(distance=1,speed=20,)],
		[robot.tasks.module_left_cw(distance=1,speed=20,),robot.tasks.module_left_cw(distance=1,speed=20,)],
		[robot.tasks.module_left_cw(distance=3,speed=20,),robot.tasks.module_left_cw(distance=3,speed=20,)],], [1, 2], self.run_color)
__runs__ = [Run1(),Run2()]
