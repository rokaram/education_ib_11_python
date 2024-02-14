login = input("Login: ")
backup_address = input("Backup address: ")

if "@" not in login and "@" in backup_address:
    print("OK")
else:
    print("Error!")
