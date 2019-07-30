a = "(){[]}("
stac = []
for i in a:
    if (i == '(' or i == '[' or i == '{'):
        if(a.index(i) != len(a) - 1):
            stac.append(i)
        else:
            thappu = a.index(i)
    elif (i == ')' or i == '}' or i == ']'):
        if(len(stac) != 0):
            stac.pop()

        else:
            thappu = a.index(i)
print(stac)
print("thappu",thappu+1)



