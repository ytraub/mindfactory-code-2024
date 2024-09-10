from generator import Run

TOP_COMMENT = '"""This is a generated file. Don\'t change anything manually."""'
IMPORTS = "from robot import Robot"


class Writer:
    def __init__(self) -> None:
        self.buffer: str = ""

    def header(self) -> str:
        return f"{TOP_COMMENT}\n{IMPORTS}\n"
    
    def class_definition(self, name: str, fields: list[str]) -> str:
        return f"class {name}:\n\r\tdef __init__():\n\r\t\t{"\n\r\t\t".join(fields)}"

    def write_buffer(self, buffer: str) -> None:
        self.buffer = f"{self.buffer}{buffer}"

    def write_line_buffer(self, buffer: str) -> None:
        self.buffer = f"{self.buffer}{buffer}\n\r"

    def write(self, runs: list[Run]) -> str:
        self.write_line_buffer(self.header())
        
        for run in runs:
            self.write_line_buffer(self.class_definition(run.get_run_name(), run.get_fields()))

        return self.buffer
