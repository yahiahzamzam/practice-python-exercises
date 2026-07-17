# ordered_lst = input("Please enter your list")

a = [1, 3, 5, 30, 42, 43, 500]
b = list(a)

num = int(input("enter a number to be found"))

index = int((0.5 * (len(a)) + 1) // 1)
print(index)
pr = (len(a[index + 1:]))
addind = int((0.5 * (len(pr)) + 1) // 1)
ind = + addind
flag = True
while flag:
    if a[index] == num:
        print(f'number found at index {index + 1}')
        flag = False
    elif a[index] < num:

        print(b)
        index = int((0.5 * len(a[index + 1:])) // 1)
        print(index)
    else:

        print(b)
        index = int((0.5 * len(a[:index + 1])) // 1)
        print(index)
    break
# stop
