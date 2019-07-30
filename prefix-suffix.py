'''

Ques 2: Given a string of brackets (, ), {, }, [, ], find the position in the string where the orders of brackets breaks.

I/p: ())

O/p: 3

I/p: (){[]}(

O/p: 8

https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

'''

a = "abcab"
i = 1
j = len(a)-1
count = 0
while(i < j):
    print(a[0:i],a[j:])
    if(a[0:i] == a[j:]):
        count = i
    i += 1
    j -= 1
print(count)