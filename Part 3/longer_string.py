# Write your solution here
mes1 = input("Please type in string 1:")
mes2 = input("Please type in string 2:")
if len(mes1) > len(mes2):
    print(f"{mes1} is longer")
elif len(mes1) < len(mes2):
    print(f"{mes2} is longer")
else:
    print(f"The strings are equally long")