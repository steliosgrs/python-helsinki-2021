# write your solution here

def read_fruits():
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            
            parts = line.split(";")
            name=parts[0]
            price = float(parts[1])
            fruits[name]=price

    return fruits

if __name__ == "__main__":
    x=read_fruits()
    print(x)