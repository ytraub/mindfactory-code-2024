class AstNode:
    def __init__(self, kind: str) -> None:
        self.kind = kind


class Program(AstNode):
    def __init__(self, body: list[AstNode]) -> None:
        super().__init__("program")
        self.body = body


class Color(AstNode):
    def __init__(self, color: str) -> None:
        super().__init__("color")
        self.color = color


class Block(AstNode):
    def __init__(self, body: list[AstNode]) -> None:
        super().__init__("block")
        self.body = body


class Tasksplit(AstNode):
    def __init__(self, body: list[AstNode]) -> None:
        super().__init__("tasksplit")
        self.body = body


class Task(AstNode):
    def __init__(self, params: dict[str, int]) -> None:
        super().__init__("task")
        self.params = params