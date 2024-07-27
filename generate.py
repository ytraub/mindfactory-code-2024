import inspect
from backend.tasks import Tasks

DATA_DIRECTORY = "frontend/generated"


def main() -> None:
    methods = [
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

    if "self" in params:
        params.remove("self")

    params = list(params)

    method_params = {
        method: inspect.getfullargspec(getattr(Tasks, method)).args
        for method in dir(Tasks)
        if callable(getattr(Tasks, method)) and not method.startswith("__")
    }

    for method_param_set in method_params.values():
        if "self" in method_param_set:
            method_param_set.remove("self")

    with open(f"{DATA_DIRECTORY}/data.py", "w+") as data:
        data.write(f"TASKS={methods}\n")
        data.write(f"PARAMS={params}\n")
        data.write(f"TASK_PARAMS={method_params}\n")


if __name__ == "__main__":
    main()
