deu_count = int(input("Deu students: "))
eng_count = int(input("Eng students: "))

deu_students = set()
eng_students = set()

for _ in range(deu_count):
    deu_students.add(input("Deu student: "))

for _ in range(eng_count):
    eng_students.add(input("Eng student: "))

symm_diff = deu_students ^ eng_students

if len(symm_diff):
    print(len(symm_diff))
else:
    print("NO")
