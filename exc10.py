import random
a = [random.randint(1, 20) for _ in range(random.randint(10, 15))]
b = [random.randint(1, 20) for _ in range(random.randint(10, 15))]
c = []

c = [num for num in a if (num not in c and num in b)]

print(set(c))

c = []

for num in a:
    if num in b:
        if num not in c:
            c.append(num)

print(set(c))
