# Copy here code of line function from previous exercise

def line(x,y):
    if y=="":
        print(x*"*")
    else:
        print(x*y[0])

def square(size, character):
    # You should call function line here with proper parameters
    c=0
    while size>c:
        line(size, character)
        c+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")