'''
Input:
N and an Array
Where 0 < N < len(Array)

Example
N = 2
Array = 1, 2, 3, 3, 4, 4

Output:
To find the
Least number of unique elements after deleting N number of elements in the Array

In the above example,
After deleting N = 2 number of elements from the Array

In the above example 1, 2 should be deleted from the array

3, 3, 4, 4 will be remaining
So,
2 unique elements remaining after deleting 2 elements from the array

So, the output should be 2

'''
n = int(input())
lis = list(map(int, input().split()))
for i in range(2):
    lis.remove(lis[0])
set1 = set(lis)
print(len(set1))
