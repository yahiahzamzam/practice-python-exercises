def get_num():
    return int(input("Enter a number, please."))


def prime_indecator():
    num = get_num()
    factors = [divisor for divisor in range(2, num) if num % divisor == 0]
    if factors == []:
        return "Prime"
    else:
        return "not prime"


print(prime_indecator())
