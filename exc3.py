lst_5 = []
max_lst = []
user_lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
check = input("enter to number to be max")
for item in user_lst:
    if int(item) < 5:
        print(item)
        lst_5.append(item)
    if int(item) < int(check):
        max_lst.append(item)

print(f'numbers that are less than 5 are {lst_5}')
print(f'numbers that are less than {check} are {max_lst}')
