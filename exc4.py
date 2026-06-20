user_input = int(input("Please enter a number"))
divisors_list = [user_input, 1]
for num in range(2, user_input):
    if user_input % num == 0:
        divisors_list.append(num)

print(divisors_list)
