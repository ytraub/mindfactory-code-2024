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
		self.run_color = 'Color.NONE'
	def create_chain(self, robot):
		robot.chain([robot.tasks.set_event(index=1,),
		[robot.tasks.module_left_cw(distance=2150,speed=100,),robot.tasks.trigger_event(index=1,)],
		robot.tasks.drive_forward_gyro(distance=820,speed=40,),
		robot.tasks.wait_event(index=1,),
		robot.tasks.drive_forward_gyro(distance=1450,speed=40,),
		robot.tasks.wait_ms(time=5000,),
		robot.tasks.module_left_ccw(distance=2150,speed=100,),], self.run_color)
class Run6:
	def __init__(self):
		self.run_name = 'run6'
		self.run_color = 'Color.MAGENTA'
	def create_chain(self, robot):
		robot.chain([robot.tasks.drive_forward_gyro(distance=1610,speed=80,),
		robot.tasks.module_left_cw(distance=700,speed=100,),
		robot.tasks.drive_backward_gyro(distance=230,speed=50,),
		robot.tasks.turn_right_on_spot(angle=45,speed=10,),
		robot.tasks.drive_forward_gyro(distance=230,speed=50,),
		robot.tasks.drive_forward_gyro(distance=80,speed=10,),
		robot.tasks.module_right_ccw(distance=550,speed=100,),
		robot.tasks.wait_ms(time=400,),
		robot.tasks.set_event(index=1,),
		[robot.tasks.module_right_cw(distance=300,speed=80,),robot.tasks.module_left_ccw(distance=700,speed=100,),robot.tasks.trigger_event(index=1,)],
		robot.tasks.drive_backward_gyro(distance=415,speed=50,),
		robot.tasks.turn_left_on_spot(angle=90,speed=15,),
		robot.tasks.drive_backward_gyro(distance=820,speed=50,),
		robot.tasks.module_right_ccw(distance=260,speed=60,),
		robot.tasks.set_event(index=2,),
		[robot.tasks.wait_ms(time=500,),robot.tasks.module_right_cw(distance=80,speed=40,),robot.tasks.trigger_event(index=2,)],
		robot.tasks.drive_forward_gyro(distance=30,speed=20,),
		robot.tasks.wait_event(index=2,),
		robot.tasks.module_right_cw(distance=450,speed=100,),
		robot.tasks.drive_backward_gyro(distance=500,speed=100,),], self.run_color)
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
__runs__ = [Run1(),Run2(),Run4(),Run5(),Run6(),Run7()]
