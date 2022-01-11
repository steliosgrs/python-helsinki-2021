# Write your solution here
import random
import string

def generate_strong_password(length,flag,sp):
    chars = ['!','?','=','+','-','(',')','#',]
    if length ==2:
        passw =random.choice(string.ascii_lowercase)
        length-=1
    else:
        passw=''

    if flag == True and sp== True:
        for i in range(length):
            if i == (length-1):
                n = random.choice(string.digits)
                passw+=str(n)
            elif i == (length-2):
                c = random.choice(chars)
                passw+=str(c)
            else:
                c = random.choice(chars)
                n = random.choice(string.digits)
                x =random.choice(string.ascii_lowercase+n+c)
                passw+=str(x)


    if flag == True and sp == False:
        for i in range(length):
            if i == (length-1):
                n = random.choice(string.digits)
                passw+=str(n)
            else:
                x =random.choice(string.ascii_lowercase+string.digits)
                passw+=str(x)

    if flag == False and sp == True:
        for i in range(length):
            if i == (length-1):
                c = random.choice(chars)
                passw+=str(c)
            else:
                c = random.choice(chars)
                x =random.choice(string.ascii_lowercase+c)
                passw+=str(x)

    if flag == False and sp == False:
        for i in range(length):
            x =random.choice(string.ascii_lowercase)
            passw+=str(x)

    return passw

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5,True,False))