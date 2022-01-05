# Write your solution here
def transpose(matrix):
    num_doubled=[]
    min = 100
    i=j=0
    for row in matrix:
        # print(row)
        if i == 2:
            i=0
        for element in row:
            # print(column)
            print(element)
            temp = element
            element = matrix[j][i]
            matrix[j][i] = temp
            # temp = matrix[i][j]
            # matrix[i][j] = matrix[j][i]
            # matrix[j][i] = temp
            # print(matrix[column][j])
            if j == 2:
                j=0
            j+=1
        
        i+=1
            


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    transpose(matrix)
    print(matrix)