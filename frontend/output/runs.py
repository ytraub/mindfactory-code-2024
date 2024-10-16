"""This is a generated file. Don't change anything manually."""

class A:
	def __init__(self):
		self.run_name = 'a'
		self.run_color = 'Color.A'
	def create_chain(self, robot):
		robot.chain([robot.tasks.create_global_timer(index=0,),], self.run_color)
class B:
	def __init__(self):
		self.run_name = 'b'
		self.run_color = 'Color.B'
	def create_chain(self, robot):
		robot.chain([robot.tasks.wait_global_timer(index=0,time=10000,),
		robot.tasks.stop_global_timer(index=0,),
		robot.tasks.drive_forward(speed=20,distance=500,),], self.run_color)
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
		[robot.tasks.module_left_ccw(distance=1400,speed=100,)],
		robot.tasks.turn_left(angle=90,speed=20,),
		robot.tasks.module_left_cw(distance=500,speed=100,),
		robot.tasks.set_event(index=5,),
		[robot.tasks.wait_ms(time=100,),robot.tasks.module_left_cw(distance=100,speed=80,),robot.tasks.wait_ms(time=2000,),robot.tasks.module_left_ccw(distance=550,speed=80,),robot.tasks.trigger_event(index=5,)],
		robot.tasks.drive_forward_gyro(distance=450,speed=50,),
		robot.tasks.turn_right(angle=20,speed=15,),
		robot.tasks.drive_forward_gyro(distance=250,speed=30,),
		robot.tasks.turn_left(angle=20,speed=15,),
		robot.tasks.drive_forward_gyro(distance=250,speed=30,),
		robot.tasks.wait_event(index=5,),
		robot.tasks.module_right_ccw(distance=1500,speed=100,),
		robot.tasks.drive_forward_gyro(distance=90,speed=30,),
		robot.tasks.module_left_cw(distance=400,speed=100,),
		[robot.tasks.module_left_cw(distance=300,speed=80,)],
		robot.tasks.drive_forward_gyro(distance=480,speed=30,),
		robot.tasks.set_event(index=6,),
		[robot.tasks.module_right_cw(distance=1500,speed=100,),robot.tasks.trigger_event(index=6,)],
		robot.tasks.module_left_ccw(distance=260,speed=100,),
		robot.tasks.wait_event(index=6,),
		robot.tasks.turn_left(angle=10,speed=30,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.drive_forward_gyro(distance=250,speed=30,),
		robot.tasks.turn_left(angle=10,speed=30,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.drive_forward_gyro(distance=140,speed=30,),
		robot.tasks.turn_left(angle=30,speed=30,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.drive_forward_gyro(distance=900,speed=60,),], self.run_color)
class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'Color.RED'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=1000,speed=40,),
		robot.tasks.drive_forward_time_gyro(time=120,speed=40,),
		robot.tasks.wait_ms(time=100,),
		robot.tasks.module_left_ccw(distance=140,speed=20,),
		robot.tasks.wait_ms(time=100,),
		robot.tasks.module_left_cw(distance=120,speed=10,),
		robot.tasks.drive_backward_gyro(distance=40,speed=20,),
		robot.tasks.module_right_ccw(distance=140,speed=20,),
		robot.tasks.drive_backward_gyro(distance=1000,speed=60,),], self.run_color)
class Run4:
	def __init__(self):
		self.run_name = 'run4'
		self.run_color = 'Color.YELLOW'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=1040,speed=60,),
		robot.tasks.turn_left(angle=48,speed=30,),
		robot.tasks.drive_forward_gyro(distance=120,speed=20,),
		robot.tasks.module_right_cw(distance=1100,speed=100,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.module_right_ccw(distance=800,speed=60,),
		robot.tasks.drive_forward_gyro(distance=60,speed=20,),
		robot.tasks.module_right_cw(distance=800,speed=60,),
		robot.tasks.module_left_ccw(distance=850,speed=60,),
		robot.tasks.module_right_ccw(distance=800,speed=60,),
		robot.tasks.drive_backward_gyro(distance=120,speed=20,),
		robot.tasks.turn_right_on_spot(angle=35,speed=30,),
		robot.tasks.drive_backward_gyro(distance=1200,speed=80,),], self.run_color)
class Run5:
	def __init__(self):
		self.run_name = 'run5'
		self.run_color = 'Color.BLACK'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(speed=60,distance=1000,),], self.run_color)
class Run7:
	def __init__(self):
		self.run_name = 'run7'
		self.run_color = 'Color.WHITE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.module_left_ccw(distance=20,speed=20,),
		robot.tasks.drive_forward_gyro(distance=600,speed=50,),
		robot.tasks.module_left_cw(distance=100,speed=30,),
		robot.tasks.turn_left(angle=53,speed=30,),
		robot.tasks.drive_forward_gyro(distance=400,speed=50,),
		robot.tasks.module_left_ccw(distance=100,speed=30,),
		robot.tasks.drive_forward_gyro(distance=850,speed=50,),
		[robot.tasks.module_right_cw(distance=600,speed=30,)],
		robot.tasks.module_left_cw(distance=80,speed=30,),], self.run_color)
__runs__ = [A(),B(),Run1(),Run2(),Run4(),Run5(),Run7()]
