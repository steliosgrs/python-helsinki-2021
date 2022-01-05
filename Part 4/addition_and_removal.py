# Write your solution here
list=[]
index=0
print(f"The list is now {list}")
# nums = int(input("How many items:"))
while True:
    act = input("a(d)d, (r)emove or e(x)it:")
    if act == "d":
        list.insert(index,index+1)
        index+=1
    elif act == "r":
        list.remove(index)
        index-=1
    else:
        break    
    print(f"The list is now {list}")
        
print("Bye!")