import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_num = []

for num1 in a:
    if num1 in b and num1 not in common_num:
        common_num.append(num1)

print(common_num)


# more effiecent version

a = [random.randint(1, 100) for _ in range(random.randint(10, 15))]
b = [random.randint(1, 100) for _ in range(random.randint(10, 15))]

print(list(set(a) & set(b)))
