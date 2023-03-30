def rec(a,b):
    if b == 0:
        return a
    else:
        return rec(a+1,b-1)

a = float(input('Введите первое число:'))
b = int(input('Введите второе число:'))
print(rec(a,b))