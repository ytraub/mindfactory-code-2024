import os

from lexer import Lexer
from parser import Parser
from debug import AstPrinter

RUN_DIRECTORY = "runs"
OUTPUT_DIRECTORY = "output"


def main() -> None:
    print("Compiling runs...")

    lexer = Lexer()
    parser = Parser()
    printer = AstPrinter()

    file_buffer = '"""\nThis is a generated file. Don\'t change anything manually.\n"""\n\nfrom robot import Robot\n\n'
    run_names = []

    for filename in sorted(os.listdir(RUN_DIRECTORY)):
        if not filename.endswith(".run"):
            continue

        run_name = filename.removesuffix(".run").title()
        run_names.append(run_name)

        with open(f"{RUN_DIRECTORY}/{filename}", "r") as source:
            lexer_result = lexer.scan_source(source.read())
            if isinstance(lexer_result, str):
                log_error("Lexing", filename, lexer_result)
                return

            parser_result = parser.parse(lexer_result)
            if isinstance(parser_result, str):
                log_error("Lexing", filename, parser_result)
                return

            printer.print_ast(parser_result)

            """ run_name = filename.removesuffix(".run")
            (output, error) = compiler.compile(tokens, run_name)
            if error:
                log_error("Parsing", filename, error)
                return

            file_buffer += output
            run_names.append(run_name.title()) """

    file_buffer += list_runs(run_names)

    with open(f"{OUTPUT_DIRECTORY}/runs.py", "w+") as output:
        output.write(file_buffer)

    print("Done!\n")


def list_runs(names: list[str]) -> str:
    buffer = "\n__runs = ["

    for name in names:
        buffer += f"{name}(),"

    buffer += "]"
    return buffer


def log_error(type: str, filename: str, msg: str) -> None:
    print(f"==== ( {type} error -> {filename} ) ====\n{msg}")


if __name__ == "__main__":
    main()
