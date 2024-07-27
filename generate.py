import inspect

from backend.tasks import Tasks

DATA_DIRECTORY = "frontend/generated"


def main() -> None:
    tasks = [
        method
        for method in dir(Tasks)
        if callable(getattr(Tasks, method)) and not method.startswith("__")
    ]

    param_sets = [
        inspect.getfullargspec(getattr(Tasks, method)).args
        for method in dir(Tasks)
        if callable(getattr(Tasks, method)) and not method.startswith("__")
    ]

    params = set()

    for param_set in param_sets:
        for param in param_set:
            params.add(param)

    params.remove("self")
    params = list(params)

    with open(f"{DATA_DIRECTORY}/data.py", "w+") as data:
        data.write(f"TASKS={tasks}\nPARAMS={params}")


if __name__ == "__main__":
    main()
