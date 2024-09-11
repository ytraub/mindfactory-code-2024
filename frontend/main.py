import os

from lexer import Lexer
from parser import Parser
from generator import Generator, Run
from writer import Writer
from debug import AstPrinter

RUN_DIRECTORY = "runs"
OUTPUT_DIRECTORY = "output"
DEBUG = False

lexer = Lexer()
parser = Parser()
generator = Generator()
writer = Writer()
ast_printer = AstPrinter()

runs: list[Run] = []


def compile_file(filename: str) -> None:
    run_name = filename.removesuffix(".run")

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

        generator_result = generator.generate(run_name, parser_result)
        runs.append(generator_result)


def main() -> None:
    print("Compiling runs...")

    for filename in sorted(os.listdir(RUN_DIRECTORY)):
        if not filename.endswith(".run"):
            continue

        compile_file(filename)

    #writer_result = writer.write(runs)
    #print(writer_result)

    print("Done!\n")


def log_error(type: str, filename: str, msg: str) -> None:
    print(f"==== ( {type} error -> {filename} ) ====\n{msg}")


if __name__ == "__main__":
    main()
