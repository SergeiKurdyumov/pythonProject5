def revers(n, n2 = 0):
    n2 = n2 * 10 + n % 10
    n = n // 10
    if n == 0:
        return print(n2)
    return revers(n, n2)


revers(12345)