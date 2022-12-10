import sys
input=sys.stdin.readline

n, k = map(int, input().split())
arr=list(map(int, input().split()))
count=0
arr1=[0]*n
loc=0
tmp=0
tmp1=0
for i in arr:
    if i in arr1:
        loc+=1
        continue
    elif 0 in arr1:
        arr1[arr1.index(0)]=i
    else:
        for j in arr1:
            if j not in arr[loc:]:
                tmp=j
                break
            elif arr[loc:].index(j)>tmp1:
                tmp=j
                tmp1=arr[loc:].index(j)
        arr1[arr1.index(tmp)]=i
        tmp=tmp1=0
        count+=1
    loc+=1
print(count)