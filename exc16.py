import random
import string


def pass_gen():

    password = [random.choice(string.ascii_lowercase), random.choice(
        string.digits), random.choice(string.punctuation), random.choice(string.ascii_uppercase)]

    for _ in range(random.randint(8, 12)):
        selec = [random.choice(string.ascii_letters), random.choice(
            string.digits), random.choice(string.punctuation)]
        password.append(selec[random.randint(0, 2)])

    password_final = "".join(password)
    return password_final


print(pass_gen())
