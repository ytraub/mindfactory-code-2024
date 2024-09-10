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
    def __init__(self, block: Block) -> None:
        super().__init__("tasksplit")
        self.block = block


class Task(AstNode):
    def __init__(self, type: str, params: dict[str, int]) -> None:
        super().__init__("task")
        self.type = type
        self.params = params


class Parser:
    def __init__(self) -> None:
        self.tokens = []
        self.index = 0
        self.current_token = None

    def reset(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = 0
        self.current_token = tokens[0]

    def advance(self) -> None:
        if not self.is_at_end():
            self.index += 1
            self.current_token = self.tokens[self.index]

    def is_at_end(self) -> bool:
        return self.current_token.token_type == TokenType.EOF

    def match(self, *types: TokenType) -> bool:
        return self.current_token.token_type in types

    def match_keyword(self, keyword: str) -> bool:
        return (
            self.current_token.token_type == TokenType.KEYWORD
            and self.current_token.lexeme == keyword
        )

    def parse(self, tokens: list[Token]) -> Program | str:
        self.reset(tokens)
        body: list[AstNode] = []

        while not self.is_at_end():
            node = self.parse_statement()
            if isinstance(node, str):
                return node
            if node:
                body.append(node)

        return Program(body)

    def parse_statement(self) -> AstNode | str | None:
        if self.match_keyword("color"):
            return self.parse_color()

        if self.match(TokenType.LEFT_BRACE):
            return self.parse_block()

        if self.match_keyword("tasksplit"):
            return self.parse_tasksplit()

        if self.match(TokenType.TASK):
            return self.parse_task()

        self.advance()
        return None

    def parse_color(self) -> Color | str:
        self.advance()
        
        if self.match(TokenType.COLOR):
            color_node = Color(self.current_token.lexeme)
            self.advance()
            return color_node
        
        return self.error_at_current("Expected color expression after 'color' keyword")

    def parse_block(self) -> Block | str:
        self.advance()
        body = self.parse_block_body()
        
        if isinstance(body, str):
            return body
        
        return Block(body)

    def parse_tasksplit(self) -> Tasksplit | str:
        self.advance()
        if not self.match(TokenType.LEFT_BRACE):
            return self.error_at_current(
                "Expected '{' to open a block after 'tasksplit'"
            )
            
        self.advance()
        body = self.parse_block_body()
        
        if isinstance(body, str):
            return body
        
        return Tasksplit(Block(body))

    def parse_task(self) -> Task | str:
        type = self.current_token.lexeme
        self.advance()
        params = self.parse_task_params()
        
        if isinstance(params, str):
            return params
        
        return Task(type, params)

    def parse_block_body(self) -> list[AstNode] | str:
        body: list[AstNode] = []
        while not self.is_at_end() and not self.match(TokenType.RIGHT_BRACE):
            node = self.parse_statement()
            if isinstance(node, str):
                return node
            if node:
                body.append(node)
                
        if self.is_at_end():
            return self.error_at_current("Expected '}' to close block or tasksplit")
        
        self.advance()
        return body

    def parse_task_params(self) -> dict[str, int] | str:
        params: dict[str, int] = {}

        if not self.match(TokenType.LEFT_PAREN):
            return self.error_at_current("Expected '(' to open task parameters")

        self.advance()

        while not self.is_at_end() and not self.match(TokenType.RIGHT_PAREN):
            if self.match(TokenType.PARAM):
                key = self.current_token.lexeme
                self.advance()

                if not self.match(TokenType.EQUALS):
                    return self.error_at_current("Expected '=' after parameter key")
                
                self.advance()

                if self.match(TokenType.NUMBER):
                    params[key] = int(self.current_token.lexeme)
                else:
                    return self.error_at_current("Expected a number after '='")
                
            else:
                return self.error_at_current("Expected a parameter identifier")

            self.advance()

        if not self.match(TokenType.RIGHT_PAREN):
            return self.error_at_current("Expected ')' to close task parameters")

        self.advance()
        return params

    def error_at_current(self, msg: str) -> str:
        return self.error(self.current_token.line, msg)

    def error(self, line: int, msg: str) -> str:
        return f"[Line {line}] {msg}"
