import os

from lexer import Lexer
from parser import Parser
from generator import Generator
from debug import AstPrinter

RUN_DIRECTORY = "runs"
OUTPUT_DIRECTORY = "output"
DEBUG = False

lexer = Lexer()
parser = Parser()
generator = Generator()
ast_printer = AstPrinter()

def compile_file(filename: str) -> None:
    run_name = filename.removesuffix(".run").title()

    with open(f"{RUN_DIRECTORY}/{filename}", "r") as file:
        source = file.read()

        lexer_result = lexer.scan(source)
        if isinstance(lexer_result, str):
            log_error("Lexing", filename, lexer_result)
            return

        parser_result = parser.parse(lexer_result)
        if isinstance(parser_result, str):
            log_error("Lexing", filename, parser_result)
            return

        if DEBUG:
            ast_printer.print_ast(parser_result)

        generator_result = generator.generate(parser_result)
        print(generator_result)

def main() -> None:
    print("Compiling runs...")

    file_buffer = '"""\nThis is a generated file. Don\'t change anything manually.\n"""\n\nfrom robot import Robot\n\n'

    for filename in sorted(os.listdir(RUN_DIRECTORY)):
        if not filename.endswith(".run"):
            continue

        compile_file(filename)

    print("Done!\n")


def log_error(type: str, filename: str, msg: str) -> None:
    print(f"==== ( {type} error -> {filename} ) ====\n{msg}")


if __name__ == "__main__":
    main()
