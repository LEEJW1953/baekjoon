import sys
input=sys.stdin.readline

def check(x):
    count=0
    for i in range(n):
        if i==0:
            tmp=arr[i]
            count+=1
        else:
            if x<=(arr[i]-tmp):
                tmp=arr[i]
                count+=1
            else:
                continue
    return c<=count

def search():
    s=1
    e=arr[-1]-arr[0]
    while s<=e:
        mid=(s+e)//2
        if check(mid):
            s=mid+1
            tmp=mid
        else:
            e=mid-1
            tmp=mid-1
    return tmp

n, c = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
print(search())