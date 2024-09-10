from parser import Program, AstNode, Color, Task, Block, Tasksplit


class Writer:
    def __init__(self) -> None:
        self.buffer: str = ""

    def get_buffer(self) -> str:
        return self.buffer

    def write(self, chars: str) -> None:
        self.buffer = f"{self.buffer}{chars}"

    def write_line(self, chars: str) -> None:
        self.buffer = f"{self.buffer}{chars}\n\r"


class Run:
    def __init__(self) -> None:
        self.color: str | None = None
        self.tasks: list[str] = []
        self.params: list[dict[str, int]] = []


class Generator:
    def __init__(self) -> None:
        self.writer: Writer | None = None
        self.program: Program | None = None
        self.current_node: AstNode | None = None
        self.index: int = 0

    def reset(self, program: Program) -> None:
        self.writer = Writer()
        self.current_node = program

    def check_current_node(self, type: AstNode) -> bool:
        return isinstance(self.current_node, type)

    def color(self) -> None | str:
        if self.check_current_node(Color):
            self.writer.write_line(f"self.color = {self.current_node.color}")
        else:
            return "Expected color decleration on top of file"

    def block(self) -> None | str:
        for node in self.current_node.body:
            self.current_node = node
            self.statement()

    def tasksplit(self) -> None | str:
        pass

    def task(self) -> None | str:
        type = self.current_node.type
        params = self.current_node.params

        self.writer.write(f"{type}(")

        for key in params:
            value = params[key]
            self.writer.write(f"{key}={value},")

        self.writer.write_line(")")

    def statement(self) -> None | str:
        if self.check_current_node(Task):
            self.task()

        if self.check_current_node(Block):
            self.block()

        if self.check_current_node(Tasksplit):
            self.tasksplit()

        if self.check_current_node(Color):
            self.color()

    def generate(self, program: Program) -> str:
        self.reset(program)
        self.block()

        print(self.writer.get_buffer())
