cat_idx = -1
idx = 0
text = input("Text: ")

while True:
    text = input("Text: ")
    idx += 1

    if "кот" in text or "Кот" in text and cat_idx != -1:
        cat_idx = idx

    if text == "СТОП":
        break


print(cat_idx + 1 if cat_idx != 1 else -1)
