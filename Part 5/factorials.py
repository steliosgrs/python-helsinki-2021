# Write your solution here
def factorials(factorial):
    
    dictio={}
    index=fact=1
                
    for factorial in range(1,factorial+1):
        # print(factorial)
        # print(index)
        fact=fact*index
        dictio[factorial]=fact
        index+=1
        # print(dictio)


    return dictio


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])