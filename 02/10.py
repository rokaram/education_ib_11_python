def calc(x, y, operation):
    match operation:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/' if y != 0:
            return x / y
        case _:
            return 888888


x = float(input("x: "))
y = float(input("y: "))
operation = input("operation: ")

print(calc(x, y, operation))
