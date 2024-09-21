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
		[robot.tasks.module_left_cw(distance=500,speed=60,),robot.tasks.wait_ms(time=400,),robot.tasks.module_left_cw(distance=1300,speed=100,),robot.tasks.trigger_event(index=3,)],
		robot.tasks.drive_forward_gyro(distance=600,speed=50,),
		robot.tasks.drive_forward_gyro(distance=100,speed=10,),
		robot.tasks.wait_event(index=3,),
		robot.tasks.module_left_ccw(distance=400,speed=100,),
		robot.tasks.drive_forward_gyro(distance=50,speed=10,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.set_event(index=4,),
		[robot.tasks.module_left_ccw(distance=850,speed=100,),robot.tasks.trigger_event(index=4,)],
		robot.tasks.turn_left(angle=90,speed=20,),
		robot.tasks.set_event(index=5,),
		[robot.tasks.wait_ms(time=100,),robot.tasks.module_left_cw(distance=100,speed=80,),robot.tasks.wait_ms(time=2000,),robot.tasks.module_left_ccw(distance=500,speed=80,),robot.tasks.trigger_event(index=5,)],
		robot.tasks.drive_forward_gyro(distance=450,speed=50,),
		robot.tasks.turn_right(angle=20,speed=15,),
		robot.tasks.drive_forward_gyro(distance=250,speed=30,),
		robot.tasks.turn_left(angle=20,speed=15,),
		robot.tasks.drive_forward_gyro(distance=250,speed=30,),
		robot.tasks.wait_event(index=5,),
		robot.tasks.module_right_ccw(distance=1500,speed=100,),
		robot.tasks.drive_forward_gyro(distance=500,speed=30,),
		robot.tasks.module_right_cw(distance=1500,speed=100,),], self.run_color)
class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'Color.RED'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=2000,speed=80,),
		robot.tasks.drive_forward_gyro(distance=1000,speed=30,),
		robot.tasks.drive_backward(distance=2500,speed=50,),], self.run_color)
class Run4:
	def __init__(self):
		self.run_name = 'run4'
		self.run_color = 'Color.YELLOW'
	def create_chain(self, robot):
		robot.chain([robot.tasks.set_event(index=1,),
		[robot.tasks.module_right_ccw(distance=200,speed=30,)],
		robot.tasks.drive_forward_gyro(distance=400,speed=30,),
		robot.tasks.turn_right(angle=90,speed=30,),
		robot.tasks.drive_forward_gyro(distance=580,speed=40,),
		robot.tasks.turn_left(angle=50,speed=30,),
		robot.tasks.drive_forward_gyro(distance=200,speed=20,),
		robot.tasks.set_event(index=2,),
		[robot.tasks.module_right_cw(distance=1200,speed=100,),robot.tasks.trigger_event(index=2,)],
		robot.tasks.drive_forward_gyro(distance=80,speed=20,),
		robot.tasks.drive_forward_time_gyro(time=400,speed=20,),
		robot.tasks.drive_backward(distance=30,speed=30,),
		robot.tasks.wait_event(index=2,),], self.run_color)
class Run7:
	def __init__(self):
		self.run_name = 'run7'
		self.run_color = 'Color.WHITE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=300,speed=50,),
		robot.tasks.turn_left(angle=30,speed=20,),
		robot.tasks.drive_forward_gyro(distance=200,speed=30,),
		robot.tasks.wait_ms(time=300,),
		robot.tasks.module_left_ccw(distance=100,speed=20,),
		robot.tasks.set_event(index=1,),
		[robot.tasks.wait_ms(time=1000,),robot.tasks.module_left_cw(distance=100,speed=30,),robot.tasks.trigger_event(index=1,)],
		robot.tasks.drive_forward_gyro(distance=700,speed=50,),
		robot.tasks.drive_forward_time_gyro(time=300,speed=20,),
		robot.tasks.module_left_ccw(distance=100,speed=20,),
		robot.tasks.module_right_ccw(distance=200,speed=80,),
		robot.tasks.wait_ms(time=500,),
		robot.tasks.drive_backward(distance=100,speed=20,),], self.run_color)
__runs__ = [Run1(),Run2(),Run4(),Run7()]
