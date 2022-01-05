# write your solution here

def largest():
    high =0
    with open("numbers.txt") as new_file:
        for line in new_file:
            num = int(line)
        if high <= num:
                high=num

    return high

if __name__ == "__main__":
    x=largest()
    print(x)