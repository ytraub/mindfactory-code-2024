"""This is a generated file. Don't change anything manually."""

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'Color.BLUE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.create_global_timer(index=0,),
		robot.tasks.set_event(index=0,),
		[robot.tasks.module_left_ccw(distance=400,speed=60,),robot.tasks.wait_ms(time=500,),robot.tasks.module_left_cw(distance=400,speed=60,),robot.tasks.trigger_event(index=0,)],
		robot.tasks.drive_backward_time_gyro(time=800,speed=10,),
		robot.tasks.wait_event(index=0,),
		robot.tasks.drive_backward_time_gyro(time=300,speed=10,),
		robot.tasks.wait_ms(time=500,),
		[robot.tasks.module_right_ccw(distance=300,speed=100,)],
		robot.tasks.drive_forward_gyro(distance=115,speed=40,),
		robot.tasks.turn_left(angle=45,speed=30,),
		robot.tasks.set_event(index=1,),
		[robot.tasks.wait_ms(time=500,),robot.tasks.module_left_cw(distance=60,speed=90,),robot.tasks.trigger_event(index=1,)],
		robot.tasks.drive_forward_gyro(distance=800,speed=80,),
		robot.tasks.drive_forward_time_gyro(time=200,speed=20,),
		robot.tasks.wait_event(index=1,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.drive_backward(distance=380,speed=40,),
		robot.tasks.turn_right_on_spot(angle=45,speed=10,),
		robot.tasks.align_gyro(),
		robot.tasks.set_event(index=2,),
		[robot.tasks.wait_ms(time=400,),robot.tasks.module_left_cw(distance=400,speed=60,),robot.tasks.wait_ms(time=400,),robot.tasks.module_left_cw(distance=800,speed=100,),robot.tasks.trigger_event(index=2,)],
		robot.tasks.drive_forward_gyro(distance=575,speed=50,),
		robot.tasks.drive_forward_gyro(distance=120,speed=10,),
		robot.tasks.wait_event(index=2,),
		robot.tasks.module_left_cw(distance=250,speed=100,),
		robot.tasks.module_left_ccw(distance=300,speed=100,),
		[robot.tasks.module_left_ccw(distance=1250,speed=100,)],
		[robot.tasks.module_right_ccw(distance=300,speed=80,)],
		robot.tasks.turn_left(angle=90,speed=20,),
		robot.tasks.set_event(index=3,),
		[robot.tasks.align_gyro(),robot.tasks.trigger_event(index=3,)],
		robot.tasks.module_left_cw(distance=550,speed=100,),
		robot.tasks.wait_event(index=3,),
		robot.tasks.drive_forward_gyro(distance=450,speed=50,),
		robot.tasks.turn_right(angle=20,speed=15,),
		robot.tasks.drive_forward_gyro(distance=160,speed=30,),
		robot.tasks.turn_left(angle=20,speed=15,),
		robot.tasks.align_gyro(),
		[robot.tasks.module_left_ccw(distance=360,speed=80,)],
		robot.tasks.set_event(index=4,),
		[robot.tasks.wait_ms(time=1000,),robot.tasks.module_right_ccw(distance=530,speed=100,),robot.tasks.trigger_event(index=4,)],
		robot.tasks.drive_forward_gyro(distance=390,speed=30,),
		robot.tasks.wait_event(index=4,),
		robot.tasks.module_right_ccw(distance=920,speed=100,),
		robot.tasks.set_event(index=5,),
		[robot.tasks.wait_ms(time=100,),robot.tasks.module_left_cw(distance=600,speed=100,),robot.tasks.trigger_event(index=5,)],
		[robot.tasks.wait_ms(time=200,),robot.tasks.module_right_cw(distance=1850,speed=100,)],
		robot.tasks.drive_forward_gyro(distance=490,speed=60,),
		robot.tasks.wait_event(index=5,),
		robot.tasks.module_left_ccw(distance=900,speed=100,),
		robot.tasks.drive_forward_gyro(distance=400,speed=40,),
		robot.tasks.turn_left(angle=70,speed=30,),
		robot.tasks.drive_forward_gyro(distance=1050,speed=100,),], self.run_color)
class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'Color.GREEN'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=950,speed=100,),
		robot.tasks.module_right_ccw(distance=290,speed=100,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.drive_forward_gyro(distance=55,speed=40,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.module_left_cw(distance=200,speed=20,),
		robot.tasks.module_left_cw(distance=200,speed=100,),
		robot.tasks.wait_ms(time=600,),
		robot.tasks.drive_backward_gyro(distance=900,speed=100,),], self.run_color)
class Run3:
	def __init__(self):
		self.run_name = 'run3'
		self.run_color = 'Color.RED'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=1020,speed=100,),
		robot.tasks.turn_right(angle=70,speed=30,),
		robot.tasks.drive_forward_gyro(distance=250,speed=60,),
		robot.tasks.drive_forward_time_gyro(time=400,speed=20,),
		robot.tasks.drive_backward_gyro(distance=240,speed=50,),
		robot.tasks.turn_left_on_spot(angle=90,speed=15,),
		robot.tasks.drive_forward_gyro(distance=540,speed=80,),
		[robot.tasks.module_left_ccw(distance=320,speed=100,),robot.tasks.wait_ms(time=200,),robot.tasks.module_left_cw(distance=340,speed=100,)],
		robot.tasks.module_right_cw(distance=360,speed=100,),
		robot.tasks.module_right_ccw(distance=250,speed=100,),
		robot.tasks.drive_custom_backward(time=1850,speed_right=100,speed_left=85,),], self.run_color)
class Run4:
	def __init__(self):
		self.run_name = 'run4'
		self.run_color = 'Color.YELLOW'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=1020,speed=100,),
		robot.tasks.turn_left(angle=48,speed=30,),
		robot.tasks.drive_forward_gyro(distance=130,speed=40,),
		robot.tasks.module_right_cw(distance=150,speed=100,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.module_right_ccw(distance=800,speed=100,),
		robot.tasks.drive_forward_gyro(distance=50,speed=20,),
		robot.tasks.module_left_cw(distance=750,speed=100,),
		robot.tasks.drive_custom_backward(time=1600,speed_right=100,speed_left=66,),], self.run_color)
class Run5:
	def __init__(self):
		self.run_name = 'run5'
		self.run_color = 'Color.WHITE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=2180,speed=80,),
		robot.tasks.module_right_time_cw(time=800,speed=100,),
		robot.tasks.drive_backward_gyro(distance=193,speed=40,),
		robot.tasks.module_right_time_cw(time=800,speed=100,),
		robot.tasks.drive_backward_gyro(distance=70,speed=20,),
		robot.tasks.module_right_time_cw(time=800,speed=100,),
		robot.tasks.drive_backward_gyro(distance=90,speed=40,),
		robot.tasks.module_left_cw(distance=800,speed=100,),
		robot.tasks.module_left_time_cw(time=100,speed=100,),
		robot.tasks.wait_event(index=0,),
		robot.tasks.drive_custom_forward(time=1600,speed_right=90,speed_left=100,),], self.run_color)
class Run6:
	def __init__(self):
		self.run_name = 'run6'
		self.run_color = 'Color.MAGENTA'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=1610,speed=90,),
		robot.tasks.module_left_cw(distance=700,speed=100,),
		robot.tasks.drive_backward_gyro(distance=260,speed=50,),
		robot.tasks.turn_right_on_spot(angle=45,speed=10,),
		robot.tasks.drive_forward_gyro(distance=230,speed=40,),
		robot.tasks.drive_forward_time_gyro(time=600,speed=20,),
		robot.tasks.module_right_ccw(distance=300,speed=100,),
		robot.tasks.set_event(index=1,),
		[robot.tasks.wait_ms(time=500,),robot.tasks.module_right_cw(distance=80,speed=80,),robot.tasks.trigger_event(index=1,)],
		robot.tasks.drive_backward_gyro(distance=455,speed=60,),
		robot.tasks.turn_left_on_spot(angle=90,speed=15,),
		robot.tasks.drive_backward_gyro(distance=885,speed=60,),
		robot.tasks.module_right_ccw(distance=260,speed=60,),
		robot.tasks.drive_forward_gyro(distance=120,speed=20,),
		robot.tasks.module_right_cw(distance=170,speed=100,),
		robot.tasks.drive_forward_gyro(distance=50,speed=20,),
		robot.tasks.module_right_cw(distance=250,speed=100,),
		robot.tasks.drive_backward_gyro(distance=550,speed=100,),], self.run_color)
class Run7:
	def __init__(self):
		self.run_name = 'run7'
		self.run_color = 'Color.WHITE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=980,speed=100,),
		robot.tasks.turn_left_on_spot(angle=52,speed=20,),
		robot.tasks.drive_forward_gyro(distance=1000,speed=80,),
		[robot.tasks.module_left_cw(distance=150,speed=10,)],
		robot.tasks.drive_forward_time_gyro(time=600,speed=10,),
		robot.tasks.module_right_cw(distance=650,speed=100,),
		robot.tasks.wait_ms(time=1000,),
		robot.tasks.drive_backward_gyro(distance=150,speed=30,),], self.run_color)
__runs__ = [Run1(),Run2(),Run3(),Run4(),Run5(),Run6(),Run7()]
