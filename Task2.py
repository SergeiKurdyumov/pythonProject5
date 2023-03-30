def rec(n,sum = 0, summ = 0):
    if n == 0:
        return print(sum, summ)
    if n % 2 == 0:
        sum += 1
    else:
        summ += 1
    return rec(n // 10, sum, summ)

a = int(input('Введите число:'))
rec(a)