# """tictactoe game for 2 players
# from blogpost: http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python by  BILLY REBECCHI,
# slightly improved by Horst JENS"""
# from __future__ import print_function
#
# choices = []
#
# for x in range (0, 16) :
#     choices.append(str(x + 1))
#
# # playerOneTurn = True
# winner = False
#
# def printBoard() :
#     ( choices[0] + choices[1] + choices[2] + choices[3] )
#     ( choices[4] + choices[5] + choices[6] + choices[7])
#     ( choices[8] + choices[9] + choices[10] + choices[11])
#     ( choices[12] + choices[13] + choices[14] + choices[15])
#
# # while not winner :
# #     printBoard()
# #
# #     if playerOneTurn :
# #         print( "Player 1:")
# #     else :
# #         print( "Player 2:")
# #
# #     try:
# #         choice = int(input(">> "))
# #     except:
# #         print("please enter a valid field")
# #         continue
# #     if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
# #         print("illegal move, plase try again")
# #         continue
# #
# #     if playerOneTurn :
# #         choices[choice - 1] = 'X'
# #     else :
# #         choices[choice - 1] = 'O'
# #
# #     playerOneTurn = not playerOneTurn
#
#     for x in range (0, 4) :
#         y = x * 4
#         if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)] and choices[y] == choices[(y + 3)]) :
#             winner = True
#             printBoard()
#         if (choices[x] == choices[(x + 4)] and choices[x] == choices[(x + 8)] and choices[x] == choices[(x + 12)]) :
#             winner = True
#             printBoard()
#
#     if((choices[0] == choices[5] and choices[0] == choices[10] and choices[0] == choices[15]) or
#        (choices[3] == choices[6] and choices[3] == choices[9] and choices[3] == choices[1])) :
#         winner = True
#         printBoard()
#
# print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
# printBoard("X"+"X"+"O"+"X")("O"+"O"+"O"+"X")("X"+"X"+"O"+"X")("X"+"X"+"X"+"X")

# poker=["X","X","O","X"],["O","O","O","X"],["X","X","O","X"],["X","X","X","X"]
# for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             for l in range(4):
#                 # if(poker[i][0]==poker[j][0]==poker[k][0]==poker[l][0]):
#                 #     a=[poker,"draw"]
#                 if (poker[i][1]==poker[j][1]==poker[k][1]==poker[l][1]):
#                     a = [poker, "draw"]
#                 # elif (poker[i][2] == poker[j][2] == poker[k][2] == poker[l][2]):
#                     a = [poker, "draw"]
#                 # elif (poker[i][3] == poker[j][3] == poker[k][3] == poker[l][3]):
#                     a=[poker,"salah"]
# print(a)



# choices = []
#
# for x in range (0, 16) :
#      choices.append(str(x + 1))
#
#      def printBoard():
#          print( choices[0] + choices[1] + choices[2] + choices[3] )
#          print( choices[4] + choices[5] + choices[6] + choices[7])
#          print( choices[8] + choices[9] + choices[10] + choices[11])
#          print( choices[12] + choices[13] + choices[14] + choices[15])
#
#      for x in range (0, 4) :
#          y = x * 4
#          if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)] and choices[y] == choices[(y + 3)]) :
#              winner = True
#              printBoard()
#          if (choices[x] == choices[(x + 4)] and choices[x] == choices[(x + 8)] and choices[x] == choices[(x + 12)]) :
#              winner = True
#              printBoard()
#      if((choices[0] == choices[5] and choices[0] == choices[10] and choices[0] == choices[15]) or
#         (choices[3] == choices[6] and choices[3] == choices[9] and choices[3] == choices[1])) :
#          winner = True
#          printBoard()


a = ["x", "o", "x", "o"], \
    ["o", "o", "o", "-"], \
    ["-", "o", "x", "-"], \
    ["o", "-", "-", "x"]
# def tiktok(a,x,o):
b = []
if (b == []):
    for i in range(4):
        if (a[i][0] == a[i][1] == a[i][2] == a[i][3] == "x"):
            b = ["x menang"]
            if (b == ["x menang"]):
                break
        if (a[i][0] == a[i][1] == a[i][2] == a[i][3] == "o"):
            b = ["o menang"]
            if (b == "o menang"):
                break
        if (a[0][i] == a[1][i] == a[2][i] == a[3][i] == "x"):
            b = ["x menang"]
            if (b == "x menang"):
                break
        if (a[0][i] == a[1][i] == a[2][i] == a[3][i] == "o"):
            b = ["o menang"]
            if (b == "o menang"):
                break
    if (b == []):
        i = 0
        if (a[i][i] == a[i + 1][i + 1] == a[i + 2][i + 2] == a[i + 3][i + 3] == "o") and (
                a[i][i + 3] == a[i + 1][i + 2] == a[i + 2][i + 1] == a[i + 3][i] == "x"):
            b = ["draw"]
        elif (a[i][i] == a[i + 1][i + 1] == a[i + 2][i + 2] == a[i + 3][i + 3] == "x") and (
                a[i][i + 3] == a[i + 1][i + 2] == a[i + 2][i + 1] == a[i + 3][i] == "o"):
            b = ["draw"]
        elif (a[i][i] == a[i + 1][i + 1] == a[i + 2][i + 2] == a[i + 3][i + 3] == "x"):
            b = ["x menang"]
        elif (a[i][i] == a[i + 1][i + 1] == a[i + 2][i + 2] == a[i + 3][i + 3] == "o"):
            b = ["o menang"]
        elif (a[i][i+3] == a[i +1][i+2] == a[i +2][i +1] == a[i +3][i] == "o"):
            b = ["o menang"]
        elif (a[i][i+3] == a[i +1][i+2] == a[i +2][i +1] == a[i +3][i] == "x"):
            b = ["x menang"]

    if (b == []):
        b = ["permainan belum selesai"]
print(b)
