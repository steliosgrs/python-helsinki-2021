# Write your solution here
import random
import string
def generate_password(length):
    passw =''
    for i in range(length):
        x =random.choice(string.ascii_lowercase)
        passw+=str(x)
    return passw

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))