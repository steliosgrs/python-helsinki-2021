# Write your solution here
def read_input(string,min_n,max_n):
    while True:
        
        try:
            number = int(input(string))
            if number in range(min_n,max_n):
                return number
        except ValueError:
            pass
        
        print(f"You must type in an integer between {min_n} and {max_n}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)