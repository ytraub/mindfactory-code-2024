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
        buffer = []
        for block in blocks:
            buffer.append(f"[{",".join(block)}],")
         
        return f"\r\tdef create_chain(self, robot):\n\r\t\trobot.chain([{"\n\r\t\t".join(buffer)}], {str(tasksplits)}, self.run_color)"

    def class_exports(self, names: list[str]) -> str:
        buffer = []
        for name in names:
            buffer.append(f"{name}()")
        
        return f"__runs__ = [{",".join(buffer)}]"

    def write_buffer(self, buffer: str) -> None:
        self.buffer = f"{self.buffer}{buffer}"

    def write_line_buffer(self, buffer: str) -> None:
        self.buffer = f"{self.buffer}{buffer}\n\r"

    def write(self, runs: list[Run]) -> str:
        run_names = []
        self.write_line_buffer(self.header())
        
        for run in runs:
            run_names.append(run.get_run_name())
            
            self.write_line_buffer(self.class_definition(run.get_run_name(), run.get_fields()))
            self.write_line_buffer(self.create_chain(run.get_blocks(), run.get_tasksplits()))
            
        self.write_line_buffer(self.class_exports(run_names))

        return self.buffer
