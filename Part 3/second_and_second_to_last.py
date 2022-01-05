# Write your solution here
mes = input("Please type in a string: ")
amount = len(mes)

if mes[1] == mes[amount-2]:
    x= mes[1]
    print(f"The second and the second to last characters are {x}")
else:
    print(f"The second and the second to last characters are different")
