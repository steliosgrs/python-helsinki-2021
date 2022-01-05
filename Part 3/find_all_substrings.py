mes = input("Please type in a word:")
leng =len(mes)
c=0
char = input("Please type in a character:")
sub_mes=""
while leng-2>c:
    if mes[c]==char:
        sub_mes=mes[c:c+3]
        print(f"{sub_mes}")
    #else
    c+=1
 #   index = mes.find(sub_mes)
#    if index>=leng-3:
#        break
    
  #  if index >= 0:
   #     print(f"{sub_mes}")
    #else:
     #   break