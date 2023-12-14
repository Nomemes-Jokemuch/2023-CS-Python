from operator import add, mul, sub
from operator import truediv as div


def prefix_evaluate(prefix_equation: str):
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    value_stack = []
    prefix_equation = prefix_equation.split()
    while prefix_equation:
        el = prefix_equation.pop()
        if el not in ops:
            value_stack.append(int(el))
        else:
            r_val = value_stack.pop()
            l_val = value_stack.pop()
            operation = ops[el]
            value_stack.append(operation(r_val, l_val))

    return value_stack[0]

assert prefix_evaluate("+ 2 3") == 5, "Must be 5"
assert prefix_evaluate("+ - 2 3 5") == 4, "Must be 4"

def WhoAmI(symbol):
    operators = set("+-*/^()")
    return symbol not in operators


def to_prefix(equation: str) -> str:
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    prefix = []

    for symbol in reversed(equation):
        if WhoAmI(symbol):
            prefix.append(symbol)
        elif symbol == ')':
            stack.append(symbol)
        elif symbol == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()
        else:
            while stack and priority.get(stack[-1], 0) >= priority.get(symbol, 0):
                prefix.append(stack.pop())
            stack.append(symbol)

    while stack:
        prefix.append(stack.pop())

    return ''.join(reversed(prefix)).replace(" ", "").replace("", " ")


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))


print(to_prefix("1 + (2 - 3) * 2"))