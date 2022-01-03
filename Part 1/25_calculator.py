# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
oper = (input("Operation: "))
if oper =="add":
    oper="+"
    print(f"{num1} {oper} {num2} = {num1+num2}")
if oper =="multiply":
    oper="*"
    print(f"{num1} {oper} {num2} = {num1*num2}")
if oper =="subtract":
    oper="-"
    print(f"{num1} {oper} {num2} = {num1-num2}")
