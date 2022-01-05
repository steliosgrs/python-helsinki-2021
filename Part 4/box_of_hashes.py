# Copy here code of line function from previous exercise

def line(x,y):
    if y=="":
        print(x*"*")
    else:
        print(x*y[0])

def box_of_hashes(height):
    # You should call function line here with proper parameters
    c=0
    while height>c:
        line(10, "#")
        c+=1
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
