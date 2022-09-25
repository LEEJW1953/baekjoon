n, k = map(int, input().split())
arr=[]
arr1=[]
for i in range(n):
    arr.append(i+1)
a=len(arr)
i=k-1
while a!=0:
    if a<=i:
        i=i%a
    arr1.append(arr[i])
    del(arr[i])
    a=len(arr)
    i+=k-1
print('<', end='')
for i in range(n):
    if i==n-1:
        print(arr1[i], end='')
    else:
        print(arr1[i], end='')
        print(',', end=' ')
print('>')