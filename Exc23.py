with open(r"C:\Coding stuff\prime.txt", "r", encoding="utf-8") as p:
    primes = [int(line.strip()) for line in p]

with open(r"C:\Coding stuff\happy.txt", "r", encoding="utf-8") as h:
    happies = [int(line.strip()) for line in h]

overlapping = []
for num1 in primes:
    for num2 in happies:
        if num1 == num2:
            overlapping.append(num2)

print(overlapping)
