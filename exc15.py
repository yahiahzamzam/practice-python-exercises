def reverse_word():
    sent = input("Please enter your sentence")
    words = sent.split()
    rvs = words[::-1]
    rvs_sent = " ".join(rvs)
    return rvs_sent


print(reverse_word())
