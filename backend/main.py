from runtime import Task, Runtime
from robot import Robot

robot = Robot()
robot.main()




class Counter(Task):
    def __init__(self, start_value: int, end: int, name: str) -> None:
        super().__init__()

        self.current = start_value
        self.end = end
        self.name = name

    def start(self):
        print(f"{self.name} start")

    def check(self):
        print(f"{self.name}: {self.current}")
        self.current += 1

        return self.current > self.end

    def stop(self):
        print(f"{self.name} stop")


runtime = Runtime()
runtime.add_tasks([Counter(1, 10, "a"), Counter(1, 12, "b"), Counter(4, 13, "c"), Counter(6, 12, "d")])
runtime.start()
