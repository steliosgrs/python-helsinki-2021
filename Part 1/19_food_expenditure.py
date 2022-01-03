# Write your solution here
times = int(input("How many times a week do you eat at the student cafeteria?"))
price_l = float(input("The price of a typical student lunch? "))
price_gr = float(input("How much money do you spend on groceries in a week?"))
lunch_w=times*price_l
groceries_m=price_gr
daily = (lunch_w+groceries_m)/7
week = lunch_w+groceries_m
print(f"\nAverage food expenditure:\nDaily: {daily} euros \nWeekly: {week} euros")