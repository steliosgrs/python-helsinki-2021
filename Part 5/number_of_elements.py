# Write your solution here
def count_matching_elements(m,x):
    count=0
    for i in range(len(m)): 
        for j in range(len(m[i])):  
            if m[i][j]==x:
                count+=1
             

    
    return count

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))