limit = int(input("Upper limit: "))
count=0
number = 1
sum=0
mes = "The consecutive sum: "
while sum < limit :    
    nnum=(count+1)*number
    sum += nnum
    count+=1
    if sum <limit:
        mes += f"{count} + "
    else:
        mes += f"{count}"
  
print(f"{mes} = {sum}")
