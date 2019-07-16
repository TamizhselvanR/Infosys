'''

input:

134

Operatiuns:

134+
431

Output:

565

'''

ip = input()
if(ip == ip[::-1]):
    print(int(ip)*2)
else:
    while(ip != ip[::-1]):
        ip = int(ip) + int(ip[::-1])
        ip = str(ip)
    print(ip)