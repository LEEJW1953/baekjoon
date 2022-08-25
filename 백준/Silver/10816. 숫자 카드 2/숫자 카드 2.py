n=int(input())
arr=[0]*20000003
arr1=list(map(int, input().split()))
for i in range(n):
    arr[arr1[i]+10000000]+=1
m=int(input())
arr2=list(map(int, input().split()))
arr3=[]
for i in range(m):
    arr3.append(arr[arr2[i]+10000000])
for i in range(len(arr3)):
    print(arr3[i], end=' ')