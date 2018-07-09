nilai=[4,1,2,5,6,2,7,1,2,8]
for i in range(len(nilai)):
    for j in reversed(range(i)):
        if nilai[j] > nilai[j+1]:
            temp = nilai[j]
            nilai[j]=nilai[j+1]#
            nilai[j+1]=temp
print(nilai)
nilai=[]
if (nilai == []):
    for i in range(4):
        if (a[i][0] == a[i+1][1]):
            i = a[i]
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