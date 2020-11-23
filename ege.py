def f(n, a_14, a_25):
    if n == 25:
        a_25 = True
    if n == 14:
        a_14 = True
    if n == 2:
        if a_14 and not a_25:
            return 1
        else:
            return 0
    elif n < 2:
        return 0
    elif n % 2 == 0:
        return f(n // 2, a_14, a_25) + f(n - 1, a_14, a_25)
    else:
        return f(n - 1, a_14, a_25)
    
print(f(24, False, False))