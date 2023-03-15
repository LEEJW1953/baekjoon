import sys
input=sys.stdin.readline

n=int(input())
arr=[list(map(str, input().strip())) for _ in range(n)]
count1, count2 = 0, 0
for i in range(n):
    s=''.join(arr[i])
    arr1=s.split('X')
    for j in range(len(arr1)):
        if len(arr1[j])>=2:
            count1+=1
for i in range(n):
    arr1=[]
    for j in range(n):
        arr1.append(arr[j][i])
    s=''.join(arr1)
    arr2=s.split('X')
    for j in range(len(arr2)):
        if len(arr2[j])>=2:
            count2+=1
print(count1, count2)