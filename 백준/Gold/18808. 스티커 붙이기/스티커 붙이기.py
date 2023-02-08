import sys
input=sys.stdin.readline

def sticker(s):
    [r, c] = s.pop(0)
    for a in range(4):
        arr=rotate(s, a, r, c)
        for i in range(n):
            for j in range(m):
                tmp=True
                for l in arr:
                    x, y = j+l[1], i+l[0]
                    if m<=x or n<=y:
                        tmp=False
                        continue
                    if nb[y][x]==1:
                        tmp=False
                        continue
                if tmp:
                    for l in arr:
                        nb[i+l[0]][j+l[1]]=1
                    return
    return

def rotate(s, num, r, c):
    if num==0:
        return s
    elif num==1:
        arr=[]
        for i in range(len(s)):
            arr.append([s[i][1], (r-1)-s[i][0]])
        return arr
    elif num==2:
        arr=[]
        for i in range(len(s)):
            arr.append([s[i][1], (r-1)-s[i][0]])
        arr1=[]
        for i in range(len(arr)):
            arr1.append([arr[i][1], (c-1)-arr[i][0]])
        return arr1
    elif num==3:
        arr=[]
        for i in range(len(s)):
            arr.append([s[i][1], (r-1)-s[i][0]])
        arr1=[]
        for i in range(len(arr)):
            arr1.append([arr[i][1], (c-1)-arr[i][0]])
        arr2=[]
        for i in range(len(arr1)):
            arr2.append([arr1[i][1], (r-1)-arr1[i][0]])
        return arr2

n, m, k = map(int, input().split())
nb=[[0]*m for _ in range(n)]
stk=[]
for i in range(k):
    r, c = map(int, input().split())
    arr=[[r, c]]
    arr1=[list(map(int, input().split())) for _ in range(r)]
    for j in range(r):
        for l in range(c):
            if arr1[j][l]:
                arr.append([j, l])
    stk.append(arr)
for i in range(k):
    sticker(stk[i])
count=0
for i in range(n):
    count+=sum(nb[i])
print(count)