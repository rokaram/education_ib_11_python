res = 1

for _ in range(6):
    num = int(input("Enter the number: "))
    res *= num if num != 0 else 1

print(res)
