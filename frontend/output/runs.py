"""This is a generated file. Don't change anything manually."""

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'Color.BLUE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=130,speed=20,),
		robot.tasks.turn_left(angle=45,speed=30,),
		robot.tasks.set_event(index=1,),
		[robot.tasks.wait_ms(time=1400,),robot.tasks.module_left_cw(distance=500,speed=90,),robot.tasks.trigger_event(index=1,)],
		robot.tasks.drive_forward_gyro(distance=800,speed=40,),
		robot.tasks.drive_forward_time_gyro(time=200,speed=20,),
		robot.tasks.wait_event(index=1,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.set_event(index=2,),
		[robot.tasks.module_left_ccw(distance=500,speed=90,),robot.tasks.trigger_event(index=2,)],
		robot.tasks.drive_backward(distance=420,speed=30,),
		robot.tasks.wait_event(index=2,),
		robot.tasks.turn_right_on_spot(angle=45,speed=10,),
		robot.tasks.set_event(index=3,),
		[robot.tasks.module_left_cw(distance=500,speed=60,),robot.tasks.wait_ms(time=200,),robot.tasks.module_left_cw(distance=1370,speed=100,),robot.tasks.trigger_event(index=3,)],
		robot.tasks.drive_forward_gyro(distance=630,speed=50,),
		robot.tasks.drive_forward_gyro(distance=80,speed=10,),
		robot.tasks.wait_event(index=3,),], self.run_color)
class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'Color.RED'
	def create_chain(self, robot):
		robot.chain([robot.tasks.module_left_ccw(distance=500,speed=50,),], self.run_color)
__runs__ = [Run1(),Run2()]
