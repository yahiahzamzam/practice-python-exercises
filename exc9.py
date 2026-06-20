import random
guesses = 0
while True:
    random_num = random.randint(1, 9)
    print(random_num)
    flag = True
    while flag:
        user_guess = int(input("enter your guess:"))
        guesses += 1
        if user_guess > random_num:
            print("Too high")

        elif user_guess < random_num:
            print("too low")

        elif user_guess == random_num:
            flag = False
            print("Correct!")
            print(f'Number of guesses was {guesses}')

        elif user_guess == "exit":
            print(f'numner of guesses {guesses}')
            print(f"The number was {random_num}")
            break

    break
