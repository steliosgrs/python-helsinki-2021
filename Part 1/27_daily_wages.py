# Write your solution here
wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")
if day == "Sunday":
    wages = wage*hours*2
    print(f"Daily wages: {wages} euros")
else:
    wages = wage*hours
    print(f"Daily wages: {wages} euros")
