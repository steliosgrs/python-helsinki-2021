# Write your solution here
mes = input("Please type in a string: ")
amount = len(mes)

while amount > 0:
    print(mes[amount-1])
    amount-=1