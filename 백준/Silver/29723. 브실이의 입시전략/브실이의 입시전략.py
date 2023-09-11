import sys
input=sys.stdin.readline

n, m, k = map(int, input().split())
d={}
minn, maxx = 0, 0
for i in range(n):
    sub, score = map(str, input().split())
    d[sub]=int(score)
for i in range(k):
    sub=input().strip()
    score=d[sub]
    minn+=score
    maxx+=score
    del d[sub]
arr=list(d.items())
arr.sort(key=lambda x:x[1])
for i in range(m-k):
    minn+=arr[i][1]
    maxx+=arr[len(arr)-1-i][1]
print(minn, maxx)