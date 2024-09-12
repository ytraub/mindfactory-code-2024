from generator import Run

TOP_COMMENT = '"""This is a generated file. Don\'t change anything manually."""'

class Writer:
    def __init__(self) -> None:
        self.buffer: str = ""

    def header(self) -> str:
        return f"{TOP_COMMENT}\n"
    
    def class_definition(self, name: str, fields: list[str]) -> str:
        return f"class {name}:\n\r\tdef __init__(self):\n\r\t\t{"\n\r\t\t".join(fields)}"
    
    def create_chain(self, blocks: list[list[str]], tasksplits: list[int]) -> str:  
        return f"\r\tdef create_chain(self, robot):\n\r\t\trobot.chain([], self.run_color)"

    def write_buffer(self, buffer: str) -> None:
        self.buffer = f"{self.buffer}{buffer}"

    def write_line_buffer(self, buffer: str) -> None:
        self.buffer = f"{self.buffer}{buffer}\n\r"

    def write(self, runs: list[Run]) -> str:
        self.write_line_buffer(self.header())
        
        for run in runs:
            self.write_line_buffer(self.class_definition(run.get_run_name(), run.get_fields()))
            self.write_line_buffer(self.create_chain(run.get_blocks(), run.get_tasksplits()))

        return self.buffer
