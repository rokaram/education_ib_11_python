def inverse_num(num):
    return num ** -1 if abs(num) >= 0.1 ** 6 else 10 ** 6


print(inverse_num(0.5))
