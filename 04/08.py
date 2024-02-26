def countdown(num):
    if num < 0:
        return print("Пуск")

    print(f"Осталось секунд: { num }")

    countdown(num - 1)


countdown(int(input("Enter the number: ")))
