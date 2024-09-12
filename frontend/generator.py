from parser import Program, AstNode, Color, Task, Block, Tasksplit


class Run:
    def __init__(self) -> None:
        self.run_name: str | None = None
        self.fields: list[str] = []
        self.blocks: list[list[str]] = []
        self.tasksplits: list[int] = []

    def set_run_name(self, run_name: str) -> None:
        self.run_name = run_name

    def get_run_name(self) -> str:
        return self.run_name

    def get_fields(self) -> list[str]:
        return self.fields

    def get_blocks(self) -> list[str]:
        return self.blocks

    def get_tasksplits(self) -> list[int]:
        return self.tasksplits

    def add_field(self, chars: str) -> None:
        self.fields.append(chars)

    def add_block(self, chars: list[str]) -> None:
        self.blocks.append(chars)

    def add_tasksplit(self, index: int) -> None:
        self.tasksplits.append(index)


class Generator:
    def __init__(self) -> None:
        self.run: Run | None = None
        self.current_node: AstNode | None = None
        self.current_block: list[str] = []

    def reset(self, program: Program) -> None:
        self.run = Run()
        self.current_node = program
        self.current_block = []

    def check_current_node(self, type: AstNode) -> bool:
        return isinstance(self.current_node, type)

    def color(self) -> None:
        self.run.add_field(f"self.run_color = 'Color.{self.current_node.color}'")

    def add_current_block(self, task: str) -> None:
        self.current_block.append(task)

    def clear_current_block(self) -> list[str]:
        block = self.current_block
        self.current_block = []
        return block

    def block(self) -> None:
        for node in self.current_node.body:
            self.current_node = node
            self.statement()

        self.run.add_block(self.clear_current_block())

    def name(self, run_name: str) -> None:
        self.run.add_field(f"self.run_name = '{run_name}'")
        self.run.run_name = run_name.title()

    def tasksplit(self) -> None:
        self.current_node = self.current_node.block

        if self.current_block:
            self.run.add_block(self.clear_current_block())

        self.run.add_tasksplit(len(self.run.get_blocks()))
        self.block()

    def task(self) -> None:
        type = self.current_node.type
        params = self.current_node.params

        buffer = f"robot.tasks.{type}("

        for key in params:
            value = params[key]
            buffer += f"{key}={value},"

        buffer += ")"
        self.add_current_block(buffer)

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
        self.name(run_name)
        self.block()

        return self.run
