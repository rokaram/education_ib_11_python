count = int(input("Count: "))
is_cat = False

for _ in range(count):
    text = input("Text: ")

    if "кот" in text or "Кот" in text:
        is_cat = True

if is_cat:
    print("МЯУ")
else:
    print("НЕТ")
