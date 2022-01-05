# Write your solution here
def longest(strings):
    c=0
    longer=""
    high_index=0

    for string in strings:
        
        # print(string)
        # lenth = len(strings[i])
        mes1=len(string)
        # mes2=len(strings[c+1])
        if mes1 > len(longer):
            high_index=c
            longer=string
        
        if c==len(string):
            break
        c+=1
    return longer

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    # if len(strings[2]) > len(strings[1]):
    #     print(strings[2])
    print(longest(strings))