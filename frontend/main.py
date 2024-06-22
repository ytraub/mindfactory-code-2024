from lexer import Lexer
from compiler import Compiler


def main():
    lexer = Lexer()
    compiler = Compiler()

    with open("runs/test.txt", "r") as source:
        lexer.reset()
        (tokens, error) = lexer.scan_source(source.read())

        if error:
            print(error)
            return
        
        compiler.compile(tokens, "output/runs.py", "test")


if __name__ == "__main__":
    main()
