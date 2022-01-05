# Write your solution here
num = int(input("Please type in your name: "))
if num%3 == 0 and num%5 ==0:
    print("FizzBuzz")
elif num%5 ==0:
    print("Buzz")
elif num%3 ==0:
    print("Fizz")
