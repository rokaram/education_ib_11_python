count_of_cities = int(input("Count of cities: "))
cities = set()

for _ in range(count_of_cities):
    cities.add(input("City: "))

print("TRY ANOTHER" if input("City: ") in cities else "OK")
