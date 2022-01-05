mes = input("Please type in a string:")
leng =len(mes)
c=0
a=o=e=False
while leng>=c:
    if "a" in mes:
        a=True
    if "e" in mes:
        e=True
    if "o" in mes:
        o=True
    c+=1
if a==True:
    print("a found")
else:
    print("a not found")
if e==True:
    print("e found")
else:
    print("e not found")
if o==True:
    print("o found")
else:
    print("o not found")
