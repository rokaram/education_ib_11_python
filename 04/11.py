count = int(input("Count: "))

aver = 0
all_iq = 0

for i in range(1, count + 1):
    iq = int(input("IQ: "))

    all_iq += iq
    aver = all_iq // i

    if iq > aver:
        print('>')
    elif iq < aver:
        print('<')
    else:
        print('0')
