from lexer import Lexer
from compiler import Compiler


def main() -> None:
    lexer = Lexer()
    compiler = Compiler()

    file_buffer = "from robot import Robot\n"

    with open("runs/test.txt", "r") as source:
        lexer.reset()
        (tokens, error) = lexer.scan_source(source.read())

        if error:
            log_error("Lexing", "test.txt", error)
            return

        (output, error) = compiler.compile(tokens, "test")
        if error:
            log_error("Parsing", "test.txt", error)
            return

        file_buffer += output

    with open("output/runs.py", "w+") as output:
        output.write(file_buffer)


def log_error(type: str, filename: str, msg: str) -> None:
    print(f"==== ( {type} error -> {filename} ) ====\n{msg}")


if __name__ == "__main__":
    main()
