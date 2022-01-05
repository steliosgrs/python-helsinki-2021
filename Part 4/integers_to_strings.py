# Write your solution here

def formatted(my_list):
    # temp_list=[0.0,0.0,0.0,0.0]
    temp_list=[]

    for i in range(len(my_list)):
        # num = f"{i:.2f}"
        # print("WEfwef")
        # num = f"{temp_list[i]:.2f}"
        # temp_list[i]=f"{my_list[i]:.2f}"
        temp_list.append(f"{my_list[i]:.2f}")
    print(temp_list)
    print(my_list)
    return temp_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    # print(new_list)
    # print(my_list)