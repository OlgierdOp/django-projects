def add(a, b): return a + b


def mul(a, b): return a * b


def div(a, b): return a / b


def sub(a, b): return a - b


operations = {
    "add": add,
    "mul": mul,
    "sub": sub,
    "div": div
}

def handle_calculation(op, a, b):

    if op in operations:
        result = operations[op](a, b)
    else:
        result = "Niedozwolona operacja"

    return result


examples = {
    "add": ["/calculus/add/1/2", 3, "dodawanie"],
    "div": ["/calculus/div/1/2", 0.5, "dzielenie"],
    "mul": ["/calculus/mul/1/2", 2, "mnożenie"],
    "sub": ["/calculus/sub/1/2", -1, "odejmowanie"],
}
