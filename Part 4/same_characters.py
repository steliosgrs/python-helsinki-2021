# Write your solution here

def same_chars(text,x,y):
    if len(text) <= y or x>y:
        return False
    if text[x]==text[y]:
        cond = True
    else:
        cond = False
    
    
    return cond
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))