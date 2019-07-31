'''

given a string of numbeer

eg: 122453089

you have to consider number starting from 5 to 8 that is : 5308

and the add this with numbers thich are less than 5 and greater than 8

5308+1+2+2+4+9 = 5326

eg:5308

ans = 5308

'''


inp = '122453089'
coun = 0
for i in range(len(inp)):
    if(inp[i] < '5' or inp[i] > '8'):
        coun += int(inp[i])
    elif(inp[i] == '5'):
        j = inp.index('8')
        coun += int(inp[i:j+1])
        for j in range(j,len(inp)):
           if(inp[j] < '5' or inp[j] > '8'):
               coun += int(inp[j])
        break
print(coun)