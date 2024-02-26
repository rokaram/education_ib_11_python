def output_cubes(num):
    for i in range(num + 1):
        print(f"Куб числа { i } равен { i ** 3 }")


num = int(input("Enter the number: "))
output_cubes(num)
