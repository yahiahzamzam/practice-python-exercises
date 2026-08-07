def binary_search(arr_len, num):
    low = 0
    high = arr_len - 1
    while low <= high:
        mid = (low + high) // 2
        guess = input(
            f"Is {num} in index {mid}?\nYes: Y\nToo high: H\nToo low: L\n")
        if guess.upper() == "Y":
            return mid
        elif guess.upper == "H":
            high = mid
        elif guess.upper() == "L":
            low = mid
    return None


num_to_be_found = int(input("What is the number I am looking for?"))
arr_length = int(input("What is the length of the array?"))

print(binary_search(arr_length, num_to_be_found))
