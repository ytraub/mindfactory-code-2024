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
        self.run_name: str = ""

    def compile(
        self, tokens: list[Token], output_path: str, run_name: str
    ) -> str | None:
        self.tokens = tokens
        self.token_ptr = 0
        self.current_token = self.tokens[0]

        error = self.parse_color()
        if error:
            return error

        error = self.parse_block()
        if error:
            return error

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
        pass

        """ with open(output_path, "w+") as output:
            output.write(f"class {run_name.title()}:") """

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
