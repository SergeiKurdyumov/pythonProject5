def rec(a,b):
    if b == 0:
        return 1
    else:
        return a * rec(a,b-1)

a = float(input('Введите первое число:'))
b = int(input('Введите второе число:'))
print(rec(a,b))