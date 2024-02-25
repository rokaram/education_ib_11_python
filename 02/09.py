h1 = int(input("h1: "))
h2 = int(input("h2: "))
h3 = int(input("h3: "))

max_h = max(h1, h2, h3)
min_h = min(h1, h2, h3)
aver_h = h1 + h2 + h3 - max_h - min_h

print(f"Max: { max_h }")
print(f"Average: { aver_h }")
print(f"Min: { min_h }")
