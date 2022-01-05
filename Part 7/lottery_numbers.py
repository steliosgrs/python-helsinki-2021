# Write your solution here
from random import sample

def lottery_numbers(amount,lower,upper):
  
    number_pool = list(range(lower, upper))
    weekly_draw = sample(number_pool, amount)
    print(weekly_draw)
    weekly_draw.sort()
    return weekly_draw

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)