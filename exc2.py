user_num = int(input("please enter your number"))
if user_num % 2 == 0:
    if user_num % 4 == 0:
        print("this is a multiple of 4")
    else:
        print("this is an even number")
else:
    print("this is an odd number")


check = int(input("please enter a number to check with"))
if user_num % check > 0:
    print(f"Your number is not divisible by {check}")
else:
    print(f"Your number is divisible by {check}")
