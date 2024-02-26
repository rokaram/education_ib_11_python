def repeat_phrase(phrase, count):
    for _ in range(count):
        print(phrase)


phrase = input("Enter the phrase: ")
count = int(input("Enter the count: "))

repeat_phrase(phrase, count)
