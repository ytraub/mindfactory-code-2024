from lexer import Lexer


def main():
    lexer = Lexer()

    with open("runs/test.txt", "r") as source:
        lexer.reset()
        (tokens, error) = lexer.scan_source(source.read())
        print(tokens, error)


if __name__ == "__main__":
    main()
