st = "123Ab3CCcdD"
dict = {}
for i in st:
    if(ord(i) > 96 and ord(i) < 123):
        j = ord(i) - 32
        if(dict.get(j) == None):
            dict[j] = [i]
        else:
            dict[j].append(i)
    elif(ord(i) > 64 and ord(i) < 91):
        j = ord(i)
        if(dict.get(j) == None):
            dict[j] = [i]
        else:
            dict[j].append(i)
for i in range(65,91):
    if(dict.get(i) != None):
        lis = dict[i]
        lis.sort()
        for j in lis:
            print(j,end = " ")
