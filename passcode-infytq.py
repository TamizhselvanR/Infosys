lis = list(input().split(','))
for i in lis:
    name,num = i.split(':')
    length = str(len(name))
    if length in num:
        inde = num.index(length)
        while(True):
            if(inde < int(length)):
                print(name[inde])
                break
            else:
                inde -= 1
    else:
        print('x')