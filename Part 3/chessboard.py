def chessboard(x):
    i = 0
    j = 0
    while i <= x-1:
        if i % 2 != 0:
            for j in range(x):
                if j % 2 == 0:
                    print(0,end="")
                else:
                    print(1,end="")
                j +=1
        else:
            for j in range(x):
                if j % 2 ==0:
                    print(1,end="")
                else:
                    print(0,end="")
                j +=1
        i += 1
        print('')
# def chessboard(times):
#     i=0
#     j=1
#     str=times*' '

#     length=len(str)
#     # c='1'
#     for i in range(times):
#         if i%2==0:
#             c='1'
#         else:
#             c='0'
  
#         for i in range(times):
#             if i%2==0:
#                 str=str+c
#                 c='0'
#                 # str.append('1')
#                 # str.pop(times)
#             else:
#                 str=str+c
#                 c='1'
#                 # str.append('0')
#                 # str.pop(times)
        
#         print(str)  
    # temp=str
    # str.replace('1','0')
    # str.replace(' ','')
    # print(str)
    # temp.replace('0','1')
    # print(temp)
    
        # if str[length-1]=='1':
        #     str=str+'0'
        # else:
        #     str=str+'1'
        # length=len(str)
        # print(str)

            # str[length-1]=='1':
        # print(str)    
        # if i==0 and j==1:
        #     str='1'
        # else:
        #     str='0'
        # for i in range(times):
        #     if i%2== 0 and j%2==1:
        #         str=str+'0'
        #     else:
        #         str=str+'1'
        
        # # else
        # # str = times*'1'
        # # for i in range(times):
        #     print(str)
        #     j+=1

# Testing the function
if __name__ == "__main__":
    chessboard(4)
