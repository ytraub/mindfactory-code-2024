from enum import Enum

KEYWORDS = ["with", "tasksplit", "drive_straight", "module_left", "speed", "distance"]


class TokenType(Enum):
    LEFT_BRACE = 0
    RIGHT_BRACE = 1
    EQUALS = 2
    NUMBER = 3
    STRING = 4
    KEYWORD = 5
    EOF = 6


class Token:
    def __init__(self, token_type: TokenType, lexeme: str | float, line: int):
        self.token_type = token_type
        self.lexeme = lexeme
        self.line = line

    def __repr__(self):
        return f"[Token type:{self.token_type} lexeme:'{self.lexeme}' line:{self.line}]"


class Lexer:
    def __init__(self) -> None:
        self.tokens: list[Token] = []

        self.line_count: int = 1
        self.buffer: str = ""

    def scan_source(self, source: str) -> tuple[list[Token], bool]:
        source_iter = iter([*source])
        while True:
            char = next(source_iter, "\0")

            if char.isnumeric():
                while char.isnumeric():
                    self.buffer += char
                    char = next(source_iter, "\0")

                self.make_token(TokenType.NUMBER, float(self.buffer))
                self.buffer = ""

            if self.is_text(char):
                while self.is_text(char):
                    self.buffer += char
                    char = next(source_iter, "\0")

                if self.buffer in KEYWORDS:
                    self.make_token(TokenType.KEYWORD, self.buffer)

                self.buffer = ""

            if char == "\0":
                self.make_token(TokenType.EOF, char)
                break

            if self.is_whitespace(char):
                continue

            match char:
                case "{":
                    self.make_token(TokenType.LEFT_BRACE, char)
                case "}":
                    self.make_token(TokenType.RIGHT_BRACE, char)
                case "=":
                    self.make_token(TokenType.EQUALS, char)
                case _:
                    return (
                        [],
                        self.error(f"Unrecognized character found in source: {char}"),
                    )

        return (self.tokens, "")

    def reset(self):
        self.line_count: int = 1
        self.buffer: str = ""

    def is_whitespace(self, char: str) -> bool:
        if not char.isspace():
            return False

        if char == "\n":
            self.line_count += 1

        return True

    def is_text(self, char: str) -> bool:
        return char.isalpha() or char == "_"

    def error(self, msg: str) -> str:
        return f"[Line {self.line_count}] {msg}"

    def make_token(self, token_type: TokenType, lexeme: str | float):
        self.tokens.append(Token(token_type, lexeme, self.line_count))
