def validate_password(password, repeat_password):
    if len(password) < 8:
        return "Короткий"

    if "123" in password:
        return "Простой"

    if password != repeat_password:
        return "Различаются"

    return "OK"


while True:
    password = input("Enter the password: ")
    repeat_password = input("Repeat the password: ")
    result_validate = validate_password(password, repeat_password)

    print(result_validate)

    if result_validate == "OK":
        break
