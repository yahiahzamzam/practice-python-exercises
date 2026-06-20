word = input("Please enter your word")
reversed_word = []
wordlst = []
last = 0
for letter in word:
    wordlst.append(letter)
    last -= 1
    reversed_word.append(word[last])

if reversed_word == wordlst:
    print("this word is a blah blah blah")
else:
    print("this word is not blah blah blah")

# shorter method

rvs = word[::-1]
if word == rvs:
    print("this word is a blah blah blah")
else:
    print("this word is not blah blah blah")
