def fizz_buzz(a, b):
    for x in range(a, b + 1):
        if not x % 3 and not x % 5:
            print("FizzBuzz")
            continue

        if not x % 3:
            print("Fizz")
            continue

        if not x % 5:
            print("Buzz")
            continue

        print(x)


a = int(input("a: "))
b = int(input("b: "))
fizz_buzz(a, b)
