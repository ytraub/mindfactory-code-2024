"""This is a generated file. Don't change anything manually."""

class Run1:
	def __init__(self):
		self.run_name = 'run1'
		self.run_color = 'Color.BLUE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.create_global_timer(index=0,),
		robot.tasks.set_event(index=0,),
		[robot.tasks.module_left_ccw(distance=400,speed=60,),robot.tasks.wait_ms(time=200,),robot.tasks.module_left_cw(distance=400,speed=60,),robot.tasks.trigger_event(index=0,)],
		robot.tasks.drive_backward_time_gyro(time=500,speed=10,),
		robot.tasks.wait_event(index=0,),
		robot.tasks.wait_ms(time=500,),
		robot.tasks.drive_forward_gyro(distance=107,speed=40,),
		robot.tasks.turn_left(angle=45,speed=30,),
		robot.tasks.drive_forward_gyro(distance=550,speed=80,),
		[robot.tasks.module_left_cw(distance=300,speed=100,)],
		robot.tasks.drive_forward_gyro(distance=100,speed=15,),
		robot.tasks.drive_forward_gyro(distance=150,speed=30,),
		robot.tasks.drive_forward_time_gyro(time=300,speed=20,),
		[robot.tasks.wait_ms(time=600,),robot.tasks.module_left_ccw(distance=300,speed=100,)],
		robot.tasks.drive_backward(distance=535,speed=30,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.turn_right(angle=45,speed=15,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.drive_backward_time_gyro(time=800,speed=30,),
		robot.tasks.wait_ms(time=500,),
		[robot.tasks.module_left_cw(distance=250,speed=60,)],
		robot.tasks.drive_forward_gyro(distance=680,speed=60,),
		robot.tasks.set_event(index=1,),
		[robot.tasks.module_left_cw(distance=1400,speed=100,),robot.tasks.trigger_event(index=1,)],
		robot.tasks.drive_forward_gyro(distance=165,speed=10,),
		robot.tasks.wait_event(index=1,),
		robot.tasks.wait_ms(time=500,),
		robot.tasks.set_event(index=2,),
		[robot.tasks.wait_ms(time=500,),robot.tasks.drive_forward_gyro(distance=80,speed=20,),robot.tasks.trigger_event(index=2,)],
		robot.tasks.module_left_ccw(distance=400,speed=100,),
		robot.tasks.wait_ms(time=800,),
		robot.tasks.module_left_ccw(distance=1350,speed=100,),
		robot.tasks.wait_event(index=2,),
		robot.tasks.turn_left(angle=90,speed=20,),
		robot.tasks.set_event(index=3,),
		[robot.tasks.wait_ms(time=200,),robot.tasks.module_left_cw(distance=600,speed=100,),robot.tasks.wait_ms(time=1200,),robot.tasks.module_right_cw(distance=350,speed=60,),robot.tasks.trigger_event(index=3,)],
		robot.tasks.drive_forward_gyro(distance=250,speed=30,),
		robot.tasks.drive_forward_gyro(distance=900,speed=60,),
		robot.tasks.wait_event(index=3,),
		robot.tasks.module_right_cw(distance=220,speed=60,),
		[robot.tasks.module_right_ccw(distance=530,speed=60,)],
		robot.tasks.drive_forward_gyro(distance=500,speed=60,),
		robot.tasks.module_left_ccw(distance=250,speed=60,),
		robot.tasks.drive_forward_gyro(distance=400,speed=30,),
		robot.tasks.turn_left(angle=67,speed=20,),
		robot.tasks.drive_forward_gyro(distance=1000,speed=100,),], self.run_color)
class Run2:
	def __init__(self):
		self.run_name = 'run2'
		self.run_color = 'Color.GREEN'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=950,speed=100,),
		robot.tasks.module_right_ccw(distance=290,speed=100,),
		robot.tasks.drive_forward_gyro(distance=55,speed=40,),
		robot.tasks.module_left_cw(distance=400,speed=40,),
		robot.tasks.drive_backward_gyro(distance=900,speed=100,),], self.run_color)
class Run3:
	def __init__(self):
		self.run_name = 'run3'
		self.run_color = 'Color.RED'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=1005,speed=90,),
		robot.tasks.turn_right(angle=70,speed=20,),
		robot.tasks.drive_forward_gyro(distance=250,speed=40,),
		robot.tasks.drive_forward_time_gyro(time=800,speed=10,),
		robot.tasks.drive_backward_gyro(distance=245,speed=50,),
		robot.tasks.turn_left_on_spot(angle=90,speed=15,),
		robot.tasks.align_gyro(),
		robot.tasks.drive_forward_gyro(distance=500,speed=80,),
		robot.tasks.drive_forward_gyro(distance=40,speed=20,),
		[robot.tasks.module_left_ccw(distance=400,speed=100,),robot.tasks.wait_ms(time=700,),robot.tasks.module_left_time_cw(time=800,speed=60,)],
		robot.tasks.module_right_cw(distance=450,speed=100,),
		robot.tasks.drive_backward_gyro(distance=20,speed=20,),
		robot.tasks.module_left_cw(distance=200,speed=100,),
		robot.tasks.drive_custom_backward(time=1850,speed_right=100,speed_left=85,),], self.run_color)
class Run4:
	def __init__(self):
		self.run_name = 'run4'
		self.run_color = 'Color.YELLOW'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=1020,speed=100,),
		robot.tasks.turn_left(angle=48,speed=30,),
		robot.tasks.drive_forward_gyro(distance=130,speed=40,),
		robot.tasks.module_right_cw(distance=100,speed=100,),
		robot.tasks.module_right_ccw(distance=800,speed=100,),
		robot.tasks.drive_forward_gyro(distance=50,speed=20,),
		robot.tasks.module_left_cw(distance=750,speed=100,),
		robot.tasks.drive_custom_backward(time=1600,speed_right=100,speed_left=66,),], self.run_color)
class Run5:
	def __init__(self):
		self.run_name = 'run5'
		self.run_color = 'Color.WHITE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=2170,speed=90,),
		robot.tasks.module_right_time_ccw(time=700,speed=100,),
		robot.tasks.drive_backward_gyro(distance=280,speed=40,),
		robot.tasks.drive_forward_gyro(distance=25,speed=40,),
		robot.tasks.set_event(index=0,),
		[robot.tasks.wait_ms(time=1000,),robot.tasks.module_left_cw(distance=800,speed=100,),robot.tasks.trigger_event(index=0,)],
		robot.tasks.drive_backward_gyro(distance=300,speed=40,),
		robot.tasks.wait_event(index=0,),
		[robot.tasks.wait_ms(time=1000,),robot.tasks.module_left_ccw(distance=500,speed=100,)],
		robot.tasks.drive_custom_forward(time=1900,speed_right=98,speed_left=100,),], self.run_color)
class Run6:
	def __init__(self):
		self.run_name = 'run6'
		self.run_color = 'Color.MAGENTA'
	def create_chain(self, robot):
		robot.chain([robot.tasks.wait_ms(time=10,),
		[robot.tasks.wait_ms(time=200,),robot.tasks.module_left_cw(distance=400,speed=100,)],
		robot.tasks.drive_forward_gyro(distance=1610,speed=90,),
		robot.tasks.module_left_cw(distance=300,speed=100,),
		robot.tasks.drive_backward_gyro(distance=260,speed=50,),
		robot.tasks.turn_right_on_spot(angle=45,speed=10,),
		robot.tasks.wait_ms(time=200,),
		robot.tasks.drive_forward_gyro(distance=250,speed=40,),
		robot.tasks.set_event(index=0,),
		[robot.tasks.module_right_ccw(distance=300,speed=100,),robot.tasks.trigger_event(index=0,)],
		robot.tasks.drive_forward_time_gyro(time=400,speed=20,),
		robot.tasks.wait_event(index=0,),
		[robot.tasks.module_right_cw(distance=80,speed=80,)],
		robot.tasks.drive_backward_gyro(distance=410,speed=60,),
		robot.tasks.turn_left_on_spot(angle=90,speed=10,),
		robot.tasks.drive_backward_gyro(distance=840,speed=60,),
		robot.tasks.module_right_ccw(distance=260,speed=60,),
		robot.tasks.drive_forward_gyro(distance=90,speed=40,),
		robot.tasks.module_right_cw(distance=200,speed=100,),
		robot.tasks.drive_forward_gyro(distance=30,speed=20,),
		robot.tasks.module_right_cw(distance=220,speed=100,),
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
