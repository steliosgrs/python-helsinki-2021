# Write your solution here
attempts=1
while True:
    code = input("PIN: ")
    if code == "4321" and attempts ==1:
        print("Correct! It only took you one single attempt!")
        break
    elif code == "4321" and attempts>1:
        print(f"Correct! It took you {attempts} attempts")
        attempts += 1
        break
    else:
        print("Wrong")
        attempts += 1

   