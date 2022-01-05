# Write your solution here
def double_items(numbers):
    num_doubled=[]
    for num in numbers:
        num_doubled.append(num *2)

    # numbers[:] = num_doubled
    return num_doubled

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)