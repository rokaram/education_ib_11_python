count = int(input("Count: "))
res = 0

for i in range(1, count + 1):
    num = int(input("Enter the number: "))
    res += num * -1 if i % 2 == 0 else num

print(f"Plus minus res: { str(res) }")
