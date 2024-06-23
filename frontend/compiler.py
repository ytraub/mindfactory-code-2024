from lexer import Token, TokenType


class Run:
    def __init__(self, name) -> None:
        self.name = name

    def execute(self):
        pass


class Compiler:
    def __init__(self) -> None:
        self.tokens: list[Token] = []
        self.token_ptr: int = 0
        self.current_token: Token = None
        self.previous_token: Token = None

        self.run_color: str = ""
        self.output_buffer: str = ""

    def compile(
        self, tokens: list[Token], run_name: str
    ) -> tuple[str | None, str | None]:
        self.tokens = tokens
        self.token_ptr = 0
        self.current_token = self.tokens[0]

        self.write_buffer(f"class {run_name.title()}:\n")
        self.write_buffer(f"\tdef __init__(self):\n\t\tself.run_name = '{run_name}'\n")

        error = self.parse_color()
        if error:
            return (None, error)

        if self.run_color:
            self.write_buffer(f"\t\tself.run_color = '{self.run_color}'\n")
        else:
            return (None, self.error_current("Unexpected: No valid run color found"))

        self.write_buffer(f"\tdef execute(self):\n")

        error = self.parse_block()
        if error:
            return (None, error)

        return (self.output_buffer, None)

    def parse_color(self) -> str | None:
        if self.check_current_keyword("color"):
            if self.check_type(self.peek(), TokenType.COLOR):
                self.advance()
                self.run_color = self.current_token.lexeme
                self.advance()
            else:
                return self.error_current(
                    f"Expected a color after keyword: {self.current_token.lexeme}"
                )
        else:
            return self.error_current("Expected color decleration in beginning of file")

    def parse_block(self) -> str | None:
        return self.parse_task()

    def parse_task(self) -> str | None:
        task = self.current_token
        self.write_buffer(f"\t\trobot.{task.lexeme}(")
        return self.parse_params()

    def parse_params(self) -> str | None:
        self.advance()
        error = self.expect(TokenType.LEFT_PAREN)
        if error:
            return error

        while not self.check_type(self.peek(), TokenType.RIGHT_PAREN):
            self.parse_pair()

        self.output_buffer = self.output_buffer.strip(",")
        self.write_buffer(")\n")

    def parse_pair(self) -> str | None:
        self.advance()
        error = self.expect(TokenType.PARAM)
        if error:
            return error

        param = self.current_token.lexeme

        self.advance()
        error = self.expect(TokenType.EQUALS)
        if error:
            return error

        self.advance()
        match self.current_token.token_type:
            case TokenType.NUMBER:
                value = self.current_token.lexeme
                self.write_buffer(f"{param}={value},")
            case _:
                return self.error_current(
                    f"Expected: {TokenType.NUMBER}, got: {self.current_token.token_type}"
                )

    def check_type(self, token: Token, token_type: TokenType) -> bool:
        return token.token_type == token_type

    def check_keyword(self, token: Token, keyword: str) -> bool:
        return token.token_type == TokenType.KEYWORD and token.lexeme == keyword

    def check_current_type(self, token_type: TokenType) -> bool:
        return self.current_token.token_type == token_type

    def check_current_keyword(self, keyword: str) -> bool:
        return (
            self.current_token.token_type == TokenType.KEYWORD
            and self.current_token.lexeme == keyword
        )

    def expect(self, token_type: TokenType) -> str | None:
        if self.current_token.token_type != token_type:
            return self.error_current(
                f"Expected: '{token_type}', got: '{self.current_token.token_type}'"
            )

        return None

    def peek(self) -> Token:
        if self.check_current_type(TokenType.EOF):
            return self.tokens[self.token_ptr]

        return self.tokens[self.token_ptr + 1]

    def advance(self) -> None:
        self.previous_token = self.current_token
        self.token_ptr += 1
        self.current_token = self.tokens[self.token_ptr]

    def error_current(self, message) -> str:
        return self.error(self.current_token.line, message)

    def error(self, line, message) -> str:
        return f"[Line {line}] {message}"

    def write_buffer(self, msg: str) -> None:
        self.output_buffer += msg
