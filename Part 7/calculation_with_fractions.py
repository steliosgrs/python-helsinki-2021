# Write your solution here
from fractions import Fraction

def fractionate(amount):
    fra=[]
    for i in range(amount):
        fract = Fraction(1, amount)
        fra.append(fract)
    return fra

if __name__ == "__main__":
    for p in fractionate(3):
        Fraction(p)



    print(fractionate(5))
