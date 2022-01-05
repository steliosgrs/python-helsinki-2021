mes = input("Please type in a word:")
sub_mes = input("Please type in a character:")

leng =len(mes)
index = mes.find(sub_mes)

sub_leng =len(sub_mes)
sub_index = mes.find(sub_mes,sub_leng+index)

if sub_index ==-1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {sub_index}.")
