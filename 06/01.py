list1 = set()
list2 = set()

number = ''

while True:
    number = input("Number of houses 1: ")

    if number == ' ':
        break

    list1.add(number)

while True:
    number = input("Number of houses 2: ")

    if number == ' ':
        break

    list2.add(number)


intersec = list1 & list2

if len(intersec):
    for x in intersec:
        print(x)
else:
    print("EMPTY")
