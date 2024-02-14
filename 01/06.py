question_1 = input("Да или нет? ")
question_2 = input("Точно? ")

if question_1 == "Да" and question_2 == "Нет":
    print("Вы гений!")
elif question_1 == "Да" and question_2 == "Да":
    print("У вас проблемы!")
elif question_1 == "Нет" and question_2 == "Да":
    print("С вами всё хорошо!!")
elif question_1 == "Нет" and question_2 == "Нет":
    print("К вам вопроов нет!")
else:
    print("Ошибка!")
