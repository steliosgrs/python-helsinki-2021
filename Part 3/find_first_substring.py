mes = input("Please type in a word:")
leng =len(mes)
c=0

while leng>=c:
    sub_mes = input("Please type in a character:")
    index = mes.find(sub_mes)
    if index>=leng-3:
        break
    sub_mes=mes[index:index+3]
    if index >= 0:
        print(f"{sub_mes}")
        break
    else:
        break
    c+=1