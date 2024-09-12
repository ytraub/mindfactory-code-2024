"""This is a generated file. Don't change anything manually."""

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'BLUE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_backward(distance=100,speed=100,),
		robot.tasks.set_event(index=1,),
		[robot.tasks.module_right_cw(distance=5000,speed=100,),robot.tasks.module_right_cw(distance=1000,speed=100,),robot.tasks.trigger_event(index=1,)],
		[robot.tasks.module_left_cw(distance=2000,speed=100,),robot.tasks.module_left_ccw(distance=2000,speed=100,),robot.tasks.trigger_event(index=1,)],
		robot.tasks.drive_forward(distance=1000,speed=100,accel_distance=0,),
		robot.tasks.wait_event(index=1,),
		robot.tasks.turn_left(angle=90,speed=50,),], self.run_color)
class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'RED'
	def create_chain(self, robot):
		robot.chain([robot.tasks.module_left_cw(distance=4,speed=20,),
		[robot.tasks.module_left_cw(distance=1,speed=20,)],
		[robot.tasks.module_left_cw(distance=1,speed=20,),robot.tasks.module_left_cw(distance=1,speed=20,)],
		robot.tasks.module_left_cw(distance=3,speed=20,),
		robot.tasks.module_left_cw(distance=3,speed=20,),], self.run_color)
__runs__ = [Run1(),Run2()]
