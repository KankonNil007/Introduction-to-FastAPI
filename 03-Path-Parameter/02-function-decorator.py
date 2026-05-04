from typing import Callable, Any

# Decorators

def fence(func):
    def wrapper():
        print("#" * 10)
        func()
        print("#" * 10)
    return wrapper

@fence
def log():
    print("Decorated!")

log()

# Updated Decorator

def custom_fence(fence: str = "+"):
    def add_fence(func):
        def wrapper(text: str):
            print(fence * len(text))
            func(text)
            print(fence * len(text))
        return wrapper
    return add_fence

@custom_fence("-")
def log(text: str = "Decorated"):
    print(text)

log("Hello World!")

# Type Hinting for Functions

def Func1(func: Callable[[Any], float]):
    pass

# How Servers Work

routes: dict[str, Callable[[Any], Any]] = {}

def route(path: str):
    def register_route(func):
        routes[path] = func
        return func
    return register_route

@route("/Shipment")
def get_shipment():
    return "Shipment 1001, in transit"

request: str = ""

while request != "quit":
    request = input("<    ")

    if request in routes:
        response = routes[request]()
        print(response, end="\n\n")
    else:
        print("Not Found")
    