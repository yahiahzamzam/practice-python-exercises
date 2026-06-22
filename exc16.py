import random
import string


def pass_gen():
    all_char = string.ascii_lowercase + string.digits + \
        string.punctuation + string.ascii_uppercase

    password = [random.choice(string.ascii_lowercase), random.choice(
        string.digits), random.choice(string.punctuation), random.choice(string.ascii_uppercase)]

    for _ in range(random.randint(4, 8)):
        password.append(random.choice(all_char))

    random.shuffle(password)
    password_final = "".join(password)

    return password_final


print(pass_gen())


def pass_gen():
    # Step 1: Guarantee at least one of each required character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Step 2: Combine all valid characters into a single selection pool
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Step 3: Fill the rest of the password length efficiently (Targeting 8 to 12 total length)
    # Since we already have 4 characters, we need between 4 and 8 more items.
    remaining_length = random.randint(4, 8)
    password += [random.choice(all_characters)
                 for _ in range(remaining_length)]

    # Step 4: Destroy the predictable starting order by shuffling the list in-place
    random.shuffle(password)

    # Step 5: Convert the list back into a clean string layout
    return "".join(password)


print(pass_gen())
