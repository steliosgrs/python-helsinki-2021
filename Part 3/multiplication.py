# Write your solution here
num = int(input("Please type in a number: "))
i=j=1
while i <=num:
    while j <=num:
        print(f"{i} x {j} = {i*j}")
        j+=1
    j=1
    i+=1
