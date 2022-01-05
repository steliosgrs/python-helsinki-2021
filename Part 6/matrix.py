# write your solution here

def matrix_sum():
    sum_row = row_sums()
    print(sum_row)
    final_sum=0
    for num in sum_row:
        final_sum+=int(num)
    return final_sum

def matrix_max():
    maxs=[]
    mmax=0
    with open("matrix.txt") as new_file:
        for line in new_file:
        
            numbers = line.split(",")
            rmax=int(max(numbers))
            maxs.append(rmax)
            mmax=max(maxs)
            # for num in numbers:
            #     row_sum+=int(num)
            # sums.append(row_sum)
    return mmax

def row_sums ():
    sums=[]
    row_sum=0
    with open("matrix.txt") as new_file:
        for line in new_file:
        
            numbers = line.split(",")
            for num in numbers:
                row_sum+=int(num)
            sums.append(row_sum)
            row_sum=0
    return sums

if __name__ == "__main__":
    z=row_sums()
    x=matrix_sum()
    y=matrix_max()
    print(f"This is row_sums:{z}")
    print(f"This is matrix_sum:{x}")
    print(f"This is matrix_max:{y}")