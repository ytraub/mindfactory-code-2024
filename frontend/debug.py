from parser import AstNode, Program, Block, Tasksplit, Color, Task


class AstPrinter:
    def print_ast(self, node: AstNode, indent: int = 0) -> None:
        prefix = " " * indent
        if isinstance(node, Program):
            print(f"{prefix}Program:")
            for child in node.body:
                self.print_ast(child, indent + 2)
        elif isinstance(node, Block):
            print(f"{prefix}Block:")
            for child in node.body:
                self.print_ast(child, indent + 2)
        elif isinstance(node, Tasksplit):
            print(f"{prefix}Tasksplit:")
            for child in node.body:
                self.print_ast(child, indent + 2)
        elif isinstance(node, Task):
            print(f"{prefix}Task {node.type}: {node.params}")
        elif isinstance(node, Color):
            print(f"{prefix}Color: {node.color}")
        else:
            print(f"{prefix}Unknown node type: {node.kind}")
