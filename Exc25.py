def binary_search(arr_len):
    low = 0
    high = arr_len - 1
    guesses = 0
    while low <= high:
        guesses += 1
        mid = (low + high) // 2
        guess = input(
            f"Is your number in index {mid}?\nYes: Y\nToo high: H\nToo low: L\n")
        if guess.upper() == "Y":
            return mid, guesses
        elif guess.upper() == "H":
            high = mid - 1
        elif guess.upper() == "L":
            low = mid + 1
    return None


arr_length = int(input("What is the length of the array?"))

print(binary_search(arr_length))
