import utils

TASK_COOLDOWN_MS = 1

class Runtime:
    def __init__(self) -> None:
        self.tasks = []
        self.untriggered_events: list[str] = []
        
        self.timer: utils.Timer = None
        self.last_tick: int = 0

    def get_tasks(self) -> list[any]:
        return self.tasks

    def set_tasks(self, state: list[any]) -> None:
        self.tasks = state

    def add_untriggered_events(self, event_name: str) -> None:
        self.untriggered_events.append(event_name)

    def trigger_event(self, event_name: str) -> None:
        if self.check_untriggered_event(event_name):
            self.untriggered_events.remove(event_name)

    def check_untriggered_event(self, event_name: str) -> bool:
        return event_name in self.untriggered_events
    
    def start_timer(self) -> None:
        self.timer = utils.Timer()
        self.timer.start()
        
    def get_time(self) -> None:
        return self.timer.get_time()
        
    def start(self, robot) -> None:
        self.start_timer()
        
        while self.tasks:
            self.last_tick = self.get_time()
            
            task = self.tasks.pop(0)
            task_finished = task.check()

            if task_finished:
                task.stop()

                next_tasks = task.get_next_tasks()
                if next_tasks:
                    self.add_tasks(next_tasks)

                if len(self.tasks) == 1:
                    robot.end_run()
            else:
                self.tasks.append(task)
                
            while not self.timer.reached(self.last_tick + TASK_COOLDOWN_MS):
                pass
            
            self.last_tick = self.get_time()
            

    def add_tasks(self, tasks: any | list[any]) -> None:
        if type(tasks) == list:
            for task in tasks:
                task.start()
                self.tasks.append(task)
        else:
            task = tasks

            task.start()
            self.tasks.append(task)

class Chain:
    def __init__(self, start_task: any, run_color: str) -> None:
        self.start_task = start_task
        self.run_color = run_color

    def get_run_color(self) -> str:
        return self.run_color

    def get_start_task(self) -> any:
        return self.start_task

    def __str__(self) -> str:
        tasks_str = self._traverse_tasks(self.start_task)
        return f"Chain(run_color={self.run_color}, tasks=[{tasks_str}])"

    def _traverse_tasks(self, task) -> str:
        result = str(task)
        next_tasks = task.get_next_tasks()

        if isinstance(next_tasks, list):
            result += " -> [Tasksplit"
            for next_task in next_tasks:
                result += " {"
                result += f" -> {self._traverse_tasks(next_task)}"
                result += " }"

            result += "]"
        elif next_tasks:
            result += f" -> {self._traverse_tasks(next_tasks)}"

        return result

