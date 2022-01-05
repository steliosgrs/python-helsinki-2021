# Write your solution here
flag = True
while flag == True:
    print("hi")
    mes = input("Shall we continue?")
    if mes == "yes" or mes == "oui" or mes == "jawohl":
        flag = True
    elif mes=="no":
        flag = False
print("okay then")