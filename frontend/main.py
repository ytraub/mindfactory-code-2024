from lexer import Lexer
from compiler import Compiler


def main() -> None:
    lexer = Lexer()
    compiler = Compiler()

    with open("runs/test.txt", "r") as source:
        lexer.reset()
        (tokens, error) = lexer.scan_source(source.read())

        if error:
            log_error("Lexing", "test.txt", error)
            return
        
        error = compiler.compile(tokens, "output/runs.py", "test")
        if error:
            log_error("Parsing", "test.txt", error)
            return

def log_error(type: str, filename: str, msg: str) -> None:
    print(f"==== ( {type} error -> {filename} ) ====\n{msg}")


if __name__ == "__main__":
    main()
