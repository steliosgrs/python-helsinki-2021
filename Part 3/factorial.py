# Write your solution here

num = int(input("Please type in a number: "))
temp=num
while num > 0:
    index=prod=1
    fact=1
    while temp >= index:
        fact=fact*index
         
        index+=1
    print(f"The factorial of the number {num} is {fact}")    
    num = int(input("Please type in a number: "))
    temp = num
    if num == -1 or num == 0:
        break
print(f"Thanks and bye!")