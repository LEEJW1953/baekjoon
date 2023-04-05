import sys
input=sys.stdin.readline

n, m = map(int, input().split())
mil=[]
total, count = 0, 0
for i in range(n):
    p, l = map(int, input().split())
    arr=list(map(int, input().split()))
    arr.sort(reverse=True)
    if l<=p:
        mil.append(arr[l-1])
    else:
        mil.append(1)
mil.sort()
for i in range(len(mil)):
    m-=mil[i]
    if m<0:
        break
    count+=1
print(count)