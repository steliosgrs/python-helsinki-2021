# Write your solution here

def sum_of_positives(my_list):
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
    my_list = [1, -2, 3, -4, 5]
    new_list = sum_of_positives(my_list)
    # print(new_list)
    # print(my_list)