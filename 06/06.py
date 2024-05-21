n = int(input())
m = int(input())

vn = list()
vm = list()

for _ in range(n):
    vn.append(input())

for _ in range(m):
    vm.append(input())

for x in vm:
    if x in vn:
        print("YES")
        continue

    print("NO")
