print("Quest!")

is_dead = True

q_1 = input("Choose the door: left, middle or right ")
if q_1 == "right":
    print("You guessed right! Go ahead")
    is_dead = False
elif q_1 == "left" or q_1 == "middle":
    print("You didnt guess right! You were eaten")
else:
    print("There is no such option. You were eaten")

if is_dead:
    print("It is pointless to keep plaing!")

q_2 = input("Choose the drink: left or right: ")
if is_dead:
    print("Dont choose, you are dead!")
elif q_2 == "left":
    print("You drank the lemonade! You win!")
elif q_2 == "right":
    print("You drank the poison! You lose!")
else:
    print("There is no such option")
