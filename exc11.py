def prime_indecator():
    num = int(input("Please enter a number"))
    factors = [divisor for divisor in range(2, num) if num % divisor == 0]
    if factors == []:
        return "Prime"
    else:
        return "not prime"


print(prime_indecator())
