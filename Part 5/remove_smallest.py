# Write your solution here
def remove_smallest(numbers):
    num_doubled=[]
    min = 100
    for num in numbers:
        if num < min :
            min=num
    if min in numbers:
        numbers.remove(min)




if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)