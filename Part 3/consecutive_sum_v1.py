limit = int(input("Upper limit: "))
count=0
number = 1
sum=0
while sum < limit :    
    nnum=(count+1)*number
    sum += nnum
    count+=1
print(sum)