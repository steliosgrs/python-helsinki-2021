# Write your solution here

num = int(input("Please type in a number: "))
numbers=[]
for i in range(1,num+1):
    numbers.append(i)

# print(numbers)
j=0

while j < len(numbers)-1:
    if j%2==0 or j==0:
        temp=numbers[j]
        numbers[j]=numbers[j+1]
        numbers[j+1]=temp
    j+=1

for i in numbers:
    print(i)  

