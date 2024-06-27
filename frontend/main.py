import os

from lexer import Lexer
from compiler import Compiler

RUN_DIRECTORY = "runs"


def main() -> None:
    lexer = Lexer()
    compiler = Compiler()

    file_buffer = '"""\nThis is a generated file. Don\'t change anything manually.\n"""\n\nfrom pybricks.tools import multitask\nfrom robot import Robot\n\n'

    for filename in os.listdir(RUN_DIRECTORY):
        if not filename.endswith(".run"):
            continue

        with open(f"{RUN_DIRECTORY}/{filename}", "r") as source:
            lexer.reset()
            (tokens, error) = lexer.scan_source(source.read())

            if error:
                log_error("Lexing", filename, error)
                return

            (output, error) = compiler.compile(tokens, filename.strip(".run"))
            if error:
                log_error("Parsing", filename, error)
                return

            file_buffer += output

    with open("output/runs.py", "w") as output:
        output.write(file_buffer)


def log_error(type: str, filename: str, msg: str) -> None:
    print(f"==== ( {type} error -> {filename} ) ====\n{msg}")


if __name__ == "__main__":
    main()
