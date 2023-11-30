#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    n = len(sys.argv)
    operators = ["+", "-", "*", "/"]
    result = 0

    if (n - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[1]
    b = sys.argv[3]

    for operator in operators:
        if sys.argv[2] == '+':
            result = calculator_1.add(int(a), int(b))
            print(f"{a} + {b} = {result}")
            break
        elif sys.argv[2] == '-':
            result = calculator_1.sub(int(a), int(b))
            print(f"{a} - {b} = {result}")
            break
        elif sys.argv[2] == '*':
            result = calculator_1.mul(int(a), int(b))
            print(f"{a} * {b} = {result}")
            break
        elif sys.argv[2] == '/':
            result = calculator_1.div(int(a), int(b))
            print(f"{a} / {b} = {result}")
            break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
