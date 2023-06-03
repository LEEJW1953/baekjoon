import sys
input=sys.stdin.readline

def find(x):
    if arr[x][0]!=x:
        arr[x][0]=find(arr[x][0])
    return arr[x][0]

def union(x, y):
    x=find(x)
    y=find(y)
    if x<y:
        arr[y][0]=x
    else:
        arr[x][0]=y

v, e = map(int, input().split())
arr=[]
count=0
d={}
for i in range(v+1):
    arr.append([i, 0])
for i in range(e):
    a, b = map(int, input().split())
    if (a, b) not in d and (b, a) not in d:
        d[(a, b)]=1
        arr[a][1]+=1
        arr[b][1]+=1
    union(a, b)
root=find(1)
tmp=True
for i in range(1, v+1):
    if find(i)!=root:
        tmp=False
        break
    if arr[i][1]%2:
        count+=1
if tmp:
    if count==0 or count==2:
        print('YES')
    else:
        print('NO')
else:
    print('NO')