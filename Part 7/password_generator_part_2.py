# Write your solution here
import random
import string
def generate_password(length,flag,sp):
    chars = ['!','?','=','+','-','(',')','#',]
    if length !=2:
        passw =random.choice(string.ascii_lowercase)
    else:
        passw=''
    
    for i in range(length-1):
        if flag == True and sp== True:
            for i in range(length-1):
                c = random.choice(chars)
                x =random.choice(string.ascii_lowercase+string.digits+c)
                passw+=str(x)

        if flag == True and sp == False:
            for i in range(length-1):
                x =random.choice(string.ascii_lowercase+string.digits)
                passw+=str(x)

        if flag == False and sp == True:
            for i in range(length-1):
                c = random.choice(chars)
                x =random.choice(string.ascii_lowercase+c)
                passw+=str(x)

        if flag == False and sp == False:
            x =random.choice(string.ascii_lowercase)
            passw+=str(x)
            x =random.choice(string.ascii_lowercase)
            passw+=str(x)
    return passw

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(2,False,False))
        
        # Write your solution here



'''
import random 

import string 

def generate_strong_password(num,cond1=True,cond2=True):

    passwd=""

    y=0

    speci="!?=+-()#"

    word=[]

    word.append(random.choice([x for x in string.ascii_lowercase]))

    y+=1

    if num==2:

        x=random.randint(0,1)

        if x==0:

            word.append(str(random.randint(0,9)))

            y+=1

        elif x==1:

            word.append(random.choice(speci))

            y+=1

    for i in range(num-y):

        if not cond2 and not cond1:

            word.append(random.choice(string.ascii_letters))

        elif cond1 and not cond2:

            x=random.randint(0,1)

            if x==0:

                word.append(random.choice(string.ascii_letters))

            elif x==1:

                word.append(str(random.randint(0,9)))

        elif cond2 and not cond1:

            x=random.randint(0,1)

            if x==0:

                word.append(random.choice(string.ascii_letters))

            elif x==1:

                word.append(random.choice(speci))

        elif cond1 and cond2:

            x=random.randint(0,2)

            if x==0:

                word.append(random.choice(string.ascii_lowercase))

            elif x==1:

                word.append(random.choice(speci))

            elif x==2:

                word.append(str(random.randint(0,9)))

    random.shuffle(word)

    passwd="".join(word)

    return passwd

        

if __name__=="__main__":

    for i in range(10):

        print(generate_strong_password(5, True, True))'''