# Copy here code of line function from previous exercise and use it in your solution

def line(x,y):
    if y=="":
        print(x*"*")
    else:
        print(x*y[0])

def shape(x,text1,y,text2):
    for i in range(x+1):
        line(i,text1)
    for i in range(y):
        line(x,text2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")

