from lexer import Token, TokenType


class Run:
    def __init__(self, name) -> None:
        self.name = name

    def execute(self):
        pass


class Compiler:
    def __init__(self) -> None:
        self.tokens: list[Token] = []
        self.token_iter = None
        self.current_token: Token = None
        self.previous_token: Token = None

    def compile(self, tokens: list[Token], output_path: str, run_name: str) -> None:
        self.tokens = tokens
        self.token_iter = iter(tokens)
        self.advance()
        self.advance()
        

        print(self.current_token)
        """ with open(output_path, "w+") as output:
            output.write(f"class {run_name.title()}:") """

    def advance(self) -> None:
        self.previous_token = self.current_token
        self.current_token = next(self.token_iter)
