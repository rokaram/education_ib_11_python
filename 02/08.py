def string_len(value):
    return f"Слово { value } имеет длину { len(value) }"


word = input("Enter the word: ")
print(string_len(word))
