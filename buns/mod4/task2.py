def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_pow = fast_power(a, n // 2)
        return half_pow * half_pow
    else:
        return a * fast_power(a, n - 1)
print(fast_power(int(input()), int(input())))