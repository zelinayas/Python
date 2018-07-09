import random
kartu = ["2H","2S","2W","2K","3H","3S","3W","3K","4H","4S","4W","4K","5H","5S","5W","5K","6H","6S","6W","6K"
        , "7H", "7S", "7W", "7K","8H","8S","8W","8K","9H","9S","9W","9K","10H","10S","10W","10K","JH","JS","JW","JK"
        , "QH", "QS", "QW", "QK","KH","KS","KW","KK","AH","AS","AW","AK"]

# def acak():
#     poker=[]
#     random.shuffle(kartu)
#     for i in range(0,5):
#         poker.append(kartu[i])
#     return poker

# increment = 0;
# def acak():
#     poker=[]
#     random.shuffle(kartu)
#     for i in range(0,5):
#         for j in range (0,52):
#             if (poker[0][0] != kartu[j][0]):
#                 poker.append(kartu[j])
#                 print('')
#                 increment += 1
#     print('kemungkinan : ', increment)
#     return poker

# poker=acak()
# print(poker)

#
# def tier(poker):
#     for j in range(52):
#         if (tier[j][0] != poker[i][0])
#             poker.tier(kartu[j])
#     return tier
# thrice=tier(poker)
# print(tier())
#
#

# import random
# angka = ["2","3","4","5","6","7","8","9","10","J","K","Q","A"]
# simbol = ["H","S","W","K"]
# count=0
# while count!=5:
#     i

poker=["5a","2b","2c","2d","5b"]
# poker=acak()
# print(poker)
# def thrice(poker):
i=0
a=[]
if(a==[]):
    if (poker[i][-1]==poker[i+1][-1]==poker[i+2][-1]==poker [i+3][-1]==poker[i+4][-1]):
        a=[poker,"flush"]
if(a==[]):
    for i in range(5):
        for j in range(i,i+)



        a=[poker,"flush"]
for i in range(2):
    for j in range(i+1,3):
        for k in range(j+1,4):
            for l in range(k+1,5):
                if(poker[i][0]==poker[j][0]==poker[k][0]==poker[l][0]):
                    a=[poker,"four of kind"]
if(a==[]):
    for i in range (3):
        for j in range(i+1,4):
            for k in range(j + 1, 5):
                for l in range(4):
                    for m in range(l + 1, 5):
                        if (poker[i][0]==poker[j][0]==poker[k][0])and(poker [l][0]==poker[m][0])and(poker[i][0]!=poker [l][0]):
                            a=[poker,"fullhouse"]
if(a==[]):
    for i in range(3):
        for j in range(i+1,4):
            for k in range(j+1,5):
                if (poker[i][0]==poker[j][0]==poker[k][0]):
                    a=[poker,"thrice"]
if(a==[]):
    for i in range (4):
        for j in range(i+1,5):
            for k in range(j + 1, 5):
                for l in range(k + 1, 5):
                    if (poker[i][0]==poker[j][0]!=poker[k][0]==poker[l][0]):
                        a=[poker,"two pairs"]
if(a==[]):
    for i in range (4):
        for j in range(i+1,5):
            if (poker[i][0]==poker[j][0]):
                a=[poker,"pairs"]


            # else:
            #     a=[poker,"nope"]
print(a)

# print(c)

# for i in range(3):
#     for j in range(i+1,3):
#         for k in range(j+1,5):
#             if (poker[i][0]==poker[j][0]==poker[k][0]):
#                 a=[poker,"thrice"]
#                 print(a)
#             else:
#                 b=[poker,"bukan thrice"]
# print(b)
