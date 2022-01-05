# Write your solution here
num = float(input("Please type in a number: "))
integer = int(num)
demical = float(num)
if demical>1:
    demical = float(num) - integer
print(f"Integer part: {integer}")
print(f"Decimal part: {demical}")