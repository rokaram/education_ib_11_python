def pyramid(num):
    for x in range(1, num * 2, 2):
        print(' ' * (num - 1 - x // 2) + '*' * x)


pyramid(int(input("Enter the number: ")))
