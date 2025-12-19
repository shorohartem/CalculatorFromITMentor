print("Калькулятор. Введите выражение........")

while True:
    try:
        expr = input("> ").strip()

        expr = expr.replace(" ", "")

        operators = ['+', '-', '*', '/']
        op = None
        for operator in operators:
            if operator in expr:
                op = operator
                break

        if op is None:
            print("throws Exception //Добавьте знак (+, -, *, /)")
            break

        parts = expr.split(op, 1)

        if len(parts) != 2:
            print("throws Exception //т.к. Введите два числа от 1 до 10")
            break

        a_str, b_str = parts
        if not (a_str.isdigit() and b_str.isdigit()):
            print("throws Exception //т.к. используются некорректные символы")
            break

        a, b = int(a_str), int(b_str)

        if not (1 <= a <= 10 and 1 <= b <= 10):
            print("throws Exception // Число вне диапазона от 1 до 10 включительно")
            break

        if op == '+':
            r = a + b
        elif op == '-':
            r = a - b
        elif op == '*':
            r = a * b
        elif op == '/':
            r = a // b

        print(f"{r}")

    except Exception as e:
        break
