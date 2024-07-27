import inspect

from backend.blocks import Blocks

DATA_DIRECTORY = "frontend/generated"


def main() -> None:
    blocks = [
        method
        for method in dir(Blocks)
        if callable(getattr(Blocks, method)) and not method.startswith("__")
    ]

    param_sets = [
        inspect.getfullargspec(getattr(Blocks, method)).args
        for method in dir(Blocks)
        if callable(getattr(Blocks, method)) and not method.startswith("__")
    ]

    params = set()

    for param_set in param_sets:
        for param in param_set:
            params.add(param)

    params.remove("self")
    params = list(params)

    with open(f"{DATA_DIRECTORY}/data.py", "w+") as data:
        data.write(f"TASKS={blocks}\nPARAMS={params}")


if __name__ == "__main__":
    main()
