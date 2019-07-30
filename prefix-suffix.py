'''

Ques 1: Given a string, find the longest length of a prefix which is also a suffix.

https://www.geeksforgeeks.org/longest-prefix-also-suffix/

'''

a = "cdcdcdc"
i = 1
j = len(a)-1
count = 0
while(i < len(a) and j >= 0):
    print(a[0:i],a[j:])
    if(a[0:i] == a[j:]):
        count = i+1
    i += 1
    j -= 1
print(count)