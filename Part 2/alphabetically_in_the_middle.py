# Write your solution here
let1 = input("1st letter:")
let2 = input("2st letter:")
let3 = input("3st letter:")

if let1<let3 and let1>let2 or let1<let2 and let1>let3:
    print(f"The letter in the middle is {let1}")
elif let2<let3 and let2>let1 or let2<let1 and let2>let3:
    print(f"The letter in the middle is {let2}")
else:
    print(f"The letter in the middle is {let3}")