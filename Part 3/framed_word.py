# Write your solution here
mes = input("Please type in a string:")
leng =len(mes)
tnb="*"*30
first_space=(28-leng)//2
if leng %2==0:
    sec_space=first_space
elif leng%2==1:
    sec_space=first_space+1

fs=" "*first_space
ss=" "*sec_space
print(tnb)
print(f"*{fs}{mes}{ss}*")

print(tnb)
