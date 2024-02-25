def validate_password(password, repeat_password):
    if len(password) < 8:
        return "Короткий"

    if password != repeat_password:
        return "Различаются"

    return "OK"


password = input("Enter the password: ")
repeat_password = input("Repeat the password: ")

print(validate_password(password, repeat_password))
