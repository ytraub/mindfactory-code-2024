from parser import Program, AstNode, Color, Task

class Writer:
    def __init__(self) -> None:
        self.buffer: str = ""

    def get_buffer(self) -> str:
        return self.buffer

    def write(self, chars: str) -> None:
        self.buffer = f"{self.buffer}{chars}"

    def write_line(self, chars: str) -> None:
        self.buffer = f"{self.buffer}\n\r{chars}"

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
        self.body = program.body
        self.current_node = self.body.pop(0)

    def advance(self) -> None:
        if len(self.body):
            self.current_node = self.body.pop(0)

    def check_current_node(self, type: AstNode) -> bool:
        return isinstance(self.current_node, type)

    def color(self) -> None | str:
        if self.check_current_node(Color):
            self.writer.write_line(f"self.color = {self.current_node.color}")
        else:
            return "Expected color decleration on top of file"
        
    def statement(self) -> None | str:
        if self.check_current_node(Task):
            type = self.current_node.type
            params = self.current_node.params

            print(type, params)

    def generate(self, program: Program) -> str:
        self.reset(program)

        error = self.color()
        if error:
            return error
        
        while self.current_node:
            error = self.statement()
            if error:
                return error
            
            self.advance()

