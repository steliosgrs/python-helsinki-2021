# Write your solution here
words=""
temp=""
trys=0
while True:
    word = input("Please type in a word: ")
    if word == temp :
        break
    elif word == "end":
        break
    else:
        words += word + " "
        temp = word

print(words)
  