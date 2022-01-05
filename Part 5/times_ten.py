# Write your solution here
def times_ten(start_index, end_index):
    dictio={}
    
    for start_index in range(start_index,end_index+1):
        
        dictio[start_index]=start_index*10


    return dictio


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)