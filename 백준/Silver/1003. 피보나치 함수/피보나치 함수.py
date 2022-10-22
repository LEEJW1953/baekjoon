import sys
input=sys.stdin.readline

t=int(input())
arr=[]
arr.append([1, 0])
arr.append([0, 1])
arr.append([1, 1])
arr.append([1, 2])
arr.append([2, 3])
for i in range(5, 41):
    arr1=[]
    arr1.append(arr[i-1][0]+arr[i-2][0])
    arr1.append(arr[i-1][1]+arr[i-2][1])
    arr.append(arr1)
for i in range(t):
    n=int(input())
    print(arr[n][0], arr[n][1])