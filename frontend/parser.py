from lexer import Token, TokenType


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


class Parser:
    def __init__(self) -> None:
        self.tokens = []
        self.index = 0
        self.current_token = None
        self.previous_token = None

    def reset(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = 0
        self.current_token = tokens[0]
        self.previous_token = None

    def match_current_token_type(self, token_type: TokenType) -> bool:
        return self.current_token.token_type == token_type

    def match_current_lexeme(self, lexeme: str) -> bool:
        return self.current_token.lexeme == lexeme

    def match_current_keyword(self, keyword: str) -> bool:
        return self.match_current_token_type(
            TokenType.KEYWORD
        ) and self.match_current_lexeme(keyword)

    def advance(self) -> None:
        if self.is_at_end():
            return

        self.index += 1
        self.previous_token = self.current_token
        self.current_token = self.tokens[self.index]

    def is_at_end(self) -> bool:
        self.match_current_token_type(TokenType.EOF)

    def parse(self, tokens: list[Token]) -> Program:
        self.reset(tokens)
        body: list[AstNode] = []

        while not self.is_at_end():
            if self.match_current_keyword("color"):
                self.advance()

                if self.match_current_token_type(TokenType.COLOR):
                    body.append(Color(self.current_token.lexeme))

            self.advance()

        return Program([])
