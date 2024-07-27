from backend.controller import Controller

methods = [
    method
    for method in dir(Controller)
    if callable(getattr(Controller, method)) and not method.startswith("__")
]

print(methods)
