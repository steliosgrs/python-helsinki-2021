# Write your solution here
# You can test your function by calling it within the following block
def line(x,y):
    if y=="":
        print(x*"*")
    else:
        print(x*y[0])
if __name__ == "__main__":
    line(5, "x")