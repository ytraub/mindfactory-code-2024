from lexer import Token, TokenType
from generated.data import TASK_PARAMS


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
        self.reset()
        self.tokens = tokens
        self.current_token = self.tokens[0]

        self.write_buffer(f"class {run_name.title()}:\n")
        self.write_buffer(f"\tdef __init__(self):\n\t\tself.run_name = '{run_name}'\n")

        error = self.parse_color()
        if error:
            return None, error

        if self.run_color:
            self.write_buffer(f"\t\tself.run_color = '{self.run_color}'")
        else:
            return None, self.error_current("Unexpected: No valid run color found")

        self.write_buffer(
            f"\n\r\tdef create_chain(self, robot: Robot):\r\t\t\trobot.chain(["
        )

        error = self.parse_run()
        if error:
            return None, error

        self.write_buffer("])\n\n\n")
        return self.output_buffer, None

    def reset(self) -> None:
        self.tokens = []
        self.token_ptr = 0
        self.current_token = None
        self.previous_token = None
        self.run_color = ""
        self.output_buffer = ""

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
            return self.error_current("Expected color declaration in beginning of file")

    def parse_run(self) -> str | None:
        while not self.check_type(self.peek(), TokenType.EOF):
            if self.check_current_type(TokenType.LEFT_BRACE):
                error = self.parse_block()
                if error:
                    return error
                if self.check_current_type(TokenType.EOF):
                    break
                continue
            elif self.check_current_keyword("with"):
                self.advance()
                error = self.parse_tasksplit()
                if error:
                    return error
                if self.check_current_type(TokenType.EOF):
                    break
                continue
            self.write_buffer("\n\t\t")
            error = self.parse_task()
            if error:
                return error

    def parse_block(self, in_tasksplit: bool = False) -> str | None:
        if self.check_current_type(TokenType.LEFT_BRACE):
            self.advance()
            if in_tasksplit:
                self.write_buffer("\n\t\t[")
            while not self.check_current_type(TokenType.RIGHT_BRACE):
                if self.check_current_type(TokenType.LEFT_BRACE):
                    if in_tasksplit:
                        return self.error_current("No sub blocks in tasksplit allowed")
                    error = self.parse_block()
                    if error:
                        return error
                    continue
                elif self.check_current_keyword("with"):
                    if in_tasksplit:
                        return self.error_current("No sub blocks in tasksplit allowed")
                    self.advance()
                    error = self.parse_tasksplit()
                    if error:
                        return error
                    continue
                if self.check_current_type(TokenType.EOF):
                    return self.error_current(
                        f"Unexpected {TokenType.EOF} in sub block\n  ->  Consider closing the block using '}}'"
                    )
                elif self.check_current_type(TokenType.RIGHT_BRACE):
                    self.advance()
                    break
                if not in_tasksplit:
                    self.write_buffer("\n\t\t")
                error = self.parse_task()
                if error:
                    return error

            if in_tasksplit:
                self.strip_buffer(",")
                self.write_buffer("],")
            self.advance()
        else:
            return self.error_current(
                f"Expected: {TokenType.TASK}, got {self.current_token.token_type}: {self.current_token.lexeme}"
            )

    def parse_tasksplit(self) -> str | None:
        if self.check_current_keyword("tasksplit"):
            if self.check_type(self.peek(), TokenType.LEFT_BRACE):
                self.advance()
                error = self.parse_block(in_tasksplit=True)
                if error:
                    return error
            else:
                return self.error_current("Expected block after tasksplit expression")
        else:
            return self.error_current(
                f"Expected valid parameter to 'with', got: {self.current_token.lexeme}"
            )

    def parse_task(self) -> str | None:
        error = self.expect(TokenType.TASK)
        if error:
            return error
        task = self.current_token
        self.write_buffer(f"robot.tasks.{task.lexeme}(")
        error = self.parse_params()
        if error:
            return error
        self.advance()

    def parse_params(self) -> str | None:
        self.advance()
        error = self.expect(TokenType.LEFT_PAREN)
        if error:
            return error
        task = self.previous_token
        while not self.check_type(self.peek(), TokenType.RIGHT_PAREN):
            error = self.parse_pair(task.lexeme)
            if error:
                return error
        self.strip_buffer(",")
        self.write_buffer("),")
        self.advance()

    def parse_pair(self, task: str) -> str | None:
        self.advance()
        error = self.expect(TokenType.PARAM)
        if error:
            return error
        param = self.current_token.lexeme
        if param not in TASK_PARAMS.get(task):
            return self.error_current(
                f"No param: '{param}' on task: '{task}'\n\rAvailable params: {TASK_PARAMS.get(task)}"
            )
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

    def strip_buffer(self, char: str) -> None:
        self.output_buffer = self.output_buffer.strip(char)
