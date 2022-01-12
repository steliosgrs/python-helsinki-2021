# Write your solution here
def spruce(x):
    print("a spruce!")
    row = "*"
    flag=1
    while x > 0:
        pr=x-1
        if flag == 1 :
            last= " " * pr + row
            flag =0

        print(" " * pr + row)

        row += "**"
        x -= 1
    print(last)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(2)