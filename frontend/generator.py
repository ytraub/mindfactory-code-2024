from parser import Program, AstNode, Color, Task, Block, Tasksplit


class Run:
    def __init__(self) -> None:
        self.run_name: str | None = None
        self.fields: list[str] = []
        self.tasks: list[str] = []
        self.tasksplits: dict[int, int] = {}

    def set_run_name(self, run_name: str) -> None:
        self.run_name = run_name

    def add_field(self, chars: str) -> None:
        self.fields.append(chars)

    def add_tasks(self, chars: list[str]) -> None:
        self.tasks.append(chars)

    def add_tasksplit(self, start: int, end: int) -> None:
        self.tasksplits[start] = end


class Generator:
    def __init__(self) -> None:
        self.run: Run | None = None
        self.current_node: AstNode | None = None

    def reset(self, program: Program) -> None:
        self.run = Run()
        self.current_node = program

    def check_current_node(self, type: AstNode) -> bool:
        return isinstance(self.current_node, type)

    def color(self) -> None:
        self.run.add_field(f"self.color = {self.current_node.color}")

    def block(self) -> None:
        for node in self.current_node.body:
            self.current_node = node
            self.statement()

    def run_name(self, run_name: str) -> None:
        self.run.add_field(f"self.run_name = {run_name}")
        self.run.run_name = run_name.title()

    def tasksplit(self) -> None:
        start = len(self.run.tasks)

        self.current_node = self.current_node.block
        self.block()

        end = len(self.run.tasks)
        self.run.add_tasksplit(start, end)

    def task(self) -> None:
        type = self.current_node.type
        params = self.current_node.params

        buffer = f"{type}("

        for key in params:
            value = params[key]
            buffer += f"{key}={value},"

        buffer += ")"
        self.run.add_tasks(buffer)

    def statement(self) -> None:
        if self.check_current_node(Task):
            self.task()

        if self.check_current_node(Block):
            self.block()

        if self.check_current_node(Tasksplit):
            self.tasksplit()

        if self.check_current_node(Color):
            self.color()

    def generate(self, run_name: str, program: Program) -> Run:
        self.reset(program)
        self.run_name(run_name)
        self.block()

        return self.run
