days = 0

while True:
    days += 1

    if float(input("Enter the temperature: ")) >= 22:
        print(f"{ days // 7 } full weeks")
        break
