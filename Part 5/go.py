# Write your solution here

# import random
# import numpy as np
# def who_won(game_board):
#     p1=p2=non=0
#     for i in game_board:
#         for j in game_board[i]:

#             if row[j] == 1:
#                 p1+=1
#             elif row[j] ==2:
#                 p2+=1
#             elif row[j] == 0:
#                 non+=1
#     if p1 > p2:
#         # print(1)
#         return 1
#     elif p2 < p1:
#         # print(2)
#         return 2
#     else:
#         # print(0)
#         return 0
    
import random
import numpy as np
def who_won(game_board):
    p1=p2=non=0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j]== 1:
                p1+=1
            elif game_board[i][j] == 2:
                p2+=1
            elif game_board[i][j] == 0:
                non+=1
    if p1 > p2:
        # print(1)
        return 1
    elif p2 > p1:
        # print(2)
        return 2
    else:
        # print(0)
        return 0
    

if __name__ == "__main__":

    game_board=[[1, 2, 2, 2], [0, 0, 0, 1], [0, 0, 2, 1]]
    # for i in range(19):
    #     row = []
    #     for j in range(19):
    #         pwan = np.random.choice(0+1+2)
    #         # print(pwan)

    #         row.append(pwan)
    #     # print(row)
    #     game_board.append(row)
    # print(game_board)
    print(who_won(game_board))
    # who_won(game_board)
    #  if win == 1:
    #     print("0: empty square")
    # elif win ==2:
    #     print("1: player 1 game piece")
    # else:
    #     print("Tie")