def divisors(num):
    return list(filter(lambda x: num % x == 0, range(1, num + 1)))


num = int(input("Enter the num: "))
divisors_num = divisors(num)

print(" ".join(map(str, divisors_num)))
print("НЕТ" if len(divisors_num) > 2 else "Простой")
