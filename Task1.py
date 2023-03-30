def calculator():
    operation = str(input('Введите операцию:'))
    if operation == '0':
        return print("Выход из программы")
    elif operation == '+':
        x = int(input('Введите первое число:'))
        y = int(input('Введите второе число:'))
        print(x + y)
    elif operation == '-':
        x = int(input('Введите первое число:'))
        y = int(input('Введите второе число:'))
        print(x - y)
    elif operation == '*':
        x = int(input('Введите первое число:'))
        y = int(input('Введите второе число:'))
        print(x * y)
    elif operation == '/':
        x = int(input('Введите первое число:'))
        y = int(input('Введите второе число:'))
        if y == 0:
            print('На ноль делить нельзя')
        else:
            print (x / y)

    calculator()


calculator()