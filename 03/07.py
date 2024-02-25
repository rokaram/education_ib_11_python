minn = 0
maxx = 1000
attempts = 0

while True:
    attempts += 1

    if attempts > 10:
        print("More than 10 attempts. Try again.")
        break

    midd = (minn + maxx) // 2
    res = input(f"This is { midd }? Enter if your number <, > or =: ")

    match res:
        case '<':
            maxx = midd
        case '>':
            minn = midd
        case '=':
            print("Cool!")
            break
