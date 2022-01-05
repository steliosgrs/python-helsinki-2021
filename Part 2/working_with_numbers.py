# Write your solution here
sum=0
count=0
pos=0
neg=0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    else:
        count +=1
        if num >0:
            sum +=num
            pos+=1
        elif num <0:
            sum +=num
            neg+=1

if count!=0:
    mean = float(sum/count)

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")