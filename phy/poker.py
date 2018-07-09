# import random
# angka = [2,3,"4","5","6","7","8","9","10","J","Q","K","A"]
# simbol= ["H","S","D","C"]
#
# count=0
# poker=[]
# while count!=10:
#     i=random.randint(0,12)
#     j=random.randint(0,4)
#     if count==0:
#         poker.append(angka[i])
#         count+=1
#         poker.append(simbol[j])
#         count+=1
#     elif (count>1):
#         while (poker[count-2]==angka[i] and poker(count-1)==simbol[j]):
#             j=random.randint(0,4)
#         poker.append(angka[i])
#         count+=1
#         poker.append(simbol[j])
#         count+=1
# print (poker)
# tes=0
# for i in range(len(poker)-2,-1,-2):
#     for j in range (0,i-2,2):
#         cek = poker[i]
#         cek2 = poker[j]
#         if(poker[i]==poker[j]):
#             tes+=1
#
# if (tes==1):
#     print("pair")
# elif(tes==2):
#     print("thrice")

# poker3=[]
# pair=1
# for i in range(len(poker2)-2, -1, -2):
#     for j in range(0, i-2, 2):
#         cek=poker2[i]
#         cek2=poker2[j]
#         if(poker2[i]==poker2[j]):
#             poker3.append(poker2[i])
#             poker3.append(poker2[i+1])
#             poker3.append(poker2[j])
#             poker3.append(poker2[j+1])
#         for k in range(len(poker3)-2, -1, -2):
#             for l in range (0, k-2, 2):
#                 cek3 = poker3[k]
#                 cek4 = poker3[l]
#                 if(poker2[i]==poker2[j]):
#                     pair+=1
#     print("two pairs")
# elif (tes==2):
#     print("thrice")
#
poker2=["A","S","3","S","4","S","5","S","2","S"]
tes=0
poker3=[]

def cekfour(poker2):
    i=0
    four="false"
    while(i<len(poker2) and four!="true"):
        ulang=1
        j=i+2
        while(j<len(poker2) and four!="true"):
            if (poker2[i]==poker2[j]):
                ulang+=1
                if(ulang==4):
                    four="true"
            j+=2
        i+=2
    return four

def cekthrice(poker2):
    i=0
    thrice = "false"
    while(i<len(poker2) and thrice!="true"):
        ulang=1
        j=i+2
        while (j<len(poker2) and thrice!="true"):
            if(poker2[i]==poker2[j]):
                ulang+=1
                if(ulang==3):
                    thrice="true"
                j+=2
            i+=2
        return thrice

def cekpair(poker2):
    i=0
    pair="false"
    while(i<len(poker2) and pair!="true"):
        ulang = 1
        j = i+2
        while(j<len(poker2) and pair!="true"):
            if(poker2[i]==poker2[j]):
                ulang+=1
                if(ulang==2):
                    pair="true"
            j+=2
        i+=2
    return pair

# def cek2pair(poker2):
    #blm selesai
    # i = 0
    # j = 0
    # copy = []
    # count = 0
    # flag = 0
    # for i in range(0, len(poker2)):
    #     if (poker2[i] == 'J'):
    #         copy.append("11")
    #     elif (poker2[i] == 'Q'):
    #         copy.append("12")
    #     elif (poker2[i] == 'K'):
    #         copy.append("13")
    #     elif (poker2[i] == 'A'):
    #         copy.append("14")
    #     else:
    #         copy.append(poker2[i])
    # copy = sorted(copy)
    # while(j<4):
    #     tes=copy[j+1]
    #     tes2=copy[j]
    #     if int(copy[j+1]-int(copy[j]==0)
# blm selesai



# from collections import Counter
poker2=["3","H","3","S","3","D","4","c","4","H"]
# print(poker2.count("3"))
print(poker2.count(poker2[0]))

string1="2 H"
string2="3 H"
string3="3 H"
print(string1.split(" "))
if string1==string2



    i=0
    duapair="false"
    jumlahpair=0
    while(i<len(poker2) and duapair!="true"):
        ulang=1
        j=i+2
        while(j<len(poker2) and duapair!="true"):
            if(poker2[i]==poker2[j]):
                ulang+=1
                if(ulang==2):
                    ulang=1
                    jumlahpair+=1
                    if(jumlahpair==2):
                        duapair="true"
            j+=2
        i+=2
    return(duapair)

def cekfullhouse(poker2):
    i=0
    fullhouse="false"
    jumlahpair=0
    while(i<len(poker2) and fullhouse!="true"):
        ulang=1
        j=i+2
        while(j<len(poker2) and fullhouse!="true"):
            if(poker2[i]==poker2[j]):
                ulang+=1
                if(ulang==3):
                    ulang+=1
                    jumlahpair+=1
                    if(jumlahpair==2):
                        fullhouse="true"
            j+=2
        i+=2
    return(fullhouse)

def cekstraight(poker2):
    i=0
    j=0
    copy=[]
    urut=0
    straight="false"
    for i in range (0, len(poker2)):
        if(poker2[i]=='J'):
            copy.append("11")
        elif(poker2[i]=='Q'):
            copy.append("12")
        elif(poker2[i]=='K'):
            copy.append("13")
        elif(poker2[i]=='A'):
            copy.append("14")
        else:
            copy.append(poker2[i])
    copy = sorted(copy)
    while(j<4 and straight!="true"):
        tes = copy[j+1]
        tes2 = copy[j]
        if int(copy[j+1]) - int(copy[j]) == 1:
            urut+=1
            if(urut==4):
                straight="true"
        elif int(copy[j+1])- int(copy[j])== -12:
            urut += 1
            if(urut==4):
                straight="true"
        j+=1
    print(copy)
    return straight

print(poker2)
print("thrice ?", cekthrice(poker2))
print("four of kind ?", cekfour(poker2))
print("pair?", cekpair(poker2))
print("two pair?", cek2pair(poker2))
print("fullhouse?", cekfullhouse(poker2))
print("straight?", cekstraight(poker2))