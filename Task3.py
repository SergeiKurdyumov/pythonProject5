
import random


def rec(a,b):
    if b > 0:
        n = float(input('Введите число:'))
    if b == 0:
        return print("Вы не угадали ", a)
    elif n < a:
        print('ваше число меньше:')
        return rec(a, b - 1)
    elif n > a:
        print('ваше число больше:')
        return rec(a, b - 1)
    elif n == a:
        return print('Вы угадали задуманное число')


x = random.randint(0,100)
s = int(10)
rec(x,s)
