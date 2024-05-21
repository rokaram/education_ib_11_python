count = int(input("Count: "))

for _ in range(count):
    text = input("Text: ")

    if "кот" in text or "Кот" in text:
        print("МЯУ")
        break
