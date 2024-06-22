from lexer import Token


class Run:
    def __init__(self, name) -> None:
        self.name = name

    def execute(self):
        pass


class Compiler:
    def __init__(self) -> None:
        self.tokens: list[Token] = []

    def compile(self, tokens: list[Token], output_path: str, run_name: str) -> None:
        

        """ with open(output_path, "w+") as output:
            output.write(f"class {run_name.title()}:") """
