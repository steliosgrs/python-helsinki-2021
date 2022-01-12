# Write your solution here

def first_word(str):
    ind = str.index(' ')
    first = str[:ind]
    
    return first

def second_word(str):
    ind = str.index(' ')
    new_str = str[ind+1:]
    try:
        ind = new_str.index(' ')
        second = new_str[:ind]
    except ValueError:
        new_str = str[ind:]
        ind = new_str.index(' ')
        second = new_str[ind+1:]
        # print(second)
    return second 

def last_word(str):
    for i in range(len(str)):
        try: 
            ind = str.index(' ')
            str = str[ind+1:]
        except ValueError:
            break
    last = str
    return last

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # sentence = "once upon a time there was a programmer"
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))