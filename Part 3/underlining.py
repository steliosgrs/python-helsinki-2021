# Write your solution here
while True:
    mes = input("Please type in a string:")
    if mes=="":
        break
    leng = len(mes)

    c=0
    mes2=""
    print(f"{mes}")
    while leng >c :
        mes2 += "-"
        c+=1
    print(f"{mes2}")


