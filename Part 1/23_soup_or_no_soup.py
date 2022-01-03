# Write your solution here
name = input("Please tell me your name: ")
if name == "Jerry":
    print("Next please!")
else:
    soup = float(input("How many portions of soup? "))
    cost = 5.9*soup
    print(f"The total cost is {cost}") 
    print("Next please!")  