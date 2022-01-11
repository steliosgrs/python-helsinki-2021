# Write your solution here
def hash_square(times):
    str = times*'#'
    for i in range(times):
        print(str)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)