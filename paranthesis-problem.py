'''

Ques 2: Given a string of brackets (, ), {, }, [, ], find the position in the string where the orders of brackets breaks.

I/p: ())

O/p: 3



I/p: (){[]}(

O/p: 8

https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

'''
wrong = 0
a = '(((){[}}'
stac = []
for i in range(len(a)):
    if (a[i] == '(' or a[i] == '[' or a[i] == '{'):
        if(i == len(a) - 1):
            wrong = i+1
        else:
            stac.append(a[i])
    elif (a[i] == ')' or a[i] == '}' or a[i] == ']'):
        if(len(stac) != 0):
            stac.pop()

        else:
            wrong = i
print(stac)
if(wrong == 0):
    wrong = len(a) - 1
print("",wrong+1)



