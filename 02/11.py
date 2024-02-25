def deter_num(num):
    if num > 0:
        return '+'

    if num < 0:
        return '-'

    return '0'


print(deter_num(float(input("Num: "))))