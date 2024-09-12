from pybricks.parameters import Side, Button

from controller import Controller
from runtime import Runtime, Chain
from tasks import Tasks, Task


class Robot:
    def __init__(self) -> None:
        self.runtime = Runtime()
        self.controller = Controller()
        self.tasks = Tasks(self, self.controller)

        self.running = False
        self.loading = False

        self.runs = []

    def get_running(self) -> bool:
        return self.running

    def set_running(self, state: bool) -> None:
        self.running = state

    def get_loading(self) -> bool:
        return self.loading

    def set_loading(self, state: bool) -> None:
        self.loading = state

    def main(self) -> None:
        self.load_runs()
        self.setup()

    def load_runs(self) -> None:
        self.set_loading(True)
        self.runs.clear()

        self.chain([[self.tasks.start_run_with_color()]], [], "")

        from runs import __runs__

        for run in __runs__:
            run.create_chain(self)

        self.set_loading(False)

    def setup(self) -> None:
        self.controller.hub.display.orientation(Side.TOP)
        self.controller.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

        self.controller.reset_gyro_angle(0)
        self.controller.reset_motors(0)

        self.runtime.add_tasks(self.tasks.menu())
        self.runtime.start(self)

    def execute_run(self, index: int) -> None:
        self.start_run()

        if index <= len(self.runs) - 1:
            run_chain = self.runs[index]
            self.runtime.add_tasks(run_chain.start_task)
        else:
            print(
                f"Run: {index + 1} (index {index}) is not available. There are only {len(self.runs)} runs."
            )

    def interrupt_run(self) -> None:
        self.runtime.tasks.clear()
        self.end_run()

    def start_run(self) -> None:
        self.set_running(True)

        self.controller.reset_motors(0)

    def end_run(self) -> None:
        self.set_running(False)

        self.controller.brake_motors()
        self.controller.reset_motors(0)

    def chain(
        self, tasks: list[list[Task]], tasksplits: list[int], run_color: str
    ) -> Chain:
        prev_task: Task | None = None

        for i, block in enumerate(tasks):
            """ if i in tasksplits:
                # in tasksplit
                sequence = 0
                while i + sequence in tasksplits:
                    sequence += 1

                start_tasks = []
                for j in range(sequence + 1):
                    a = tasks[j]
                    b: Task | None = None
                    for c in a:
                        if b:
                            b.set_next_tasks(c)
                        
                        b = c
                        
                    start_tasks.append(a[0])
                    
                prev_task.set_next_tasks(start_tasks) """

            for task in block:
                if prev_task:
                    prev_task.set_next_tasks(task)

                prev_task = task

        self.runs.append(Chain(prev_task, run_color))
