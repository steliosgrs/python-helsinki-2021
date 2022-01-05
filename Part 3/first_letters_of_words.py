# Write your solution here
string = input("Please type in a sentence: ")
index=1
print(string[0])
while index < len(string):

    if string[index] ==" ":
        c=string[index+1]
        print(f"{c}")

    index+=1
