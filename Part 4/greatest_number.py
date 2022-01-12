# Write your solution here

def greatest_number(x,y,z):
    high=-999999
    if x > high :
        high = x
    if y > high:
        high =y
    if z > high:
        high = z

    return high
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)