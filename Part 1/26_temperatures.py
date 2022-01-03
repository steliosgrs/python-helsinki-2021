# Write your solution here
fare = int(input("Please type in a temperature (F):"))
cel = (fare-32)/1.8
print(f"{fare} degrees Fahrenheit equals {cel} degrees Celsius")
if cel < 0:
    print("Brr! It's cold in here!")
