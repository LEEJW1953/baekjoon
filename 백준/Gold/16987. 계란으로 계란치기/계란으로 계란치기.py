import sys
input=sys.stdin.readline

def crack():
    global answer
    ans=0
    for i in range(n):
        if egg[i][0]<1:
            ans+=1
    answer=max(answer, ans)
    return

def f(x):
    if x==n:
        crack()
        return
    egg1=egg[x]
    if egg1[0]<1:
        f(x+1)
        return
    tmp=True
    for i in range(n):
        if i==x:
            continue
        if egg[i][0]>0:
            tmp=False
    if tmp:
        f(x+1)
        return
    for i in range(n):
        if i==x:
            continue
        egg2=egg[i]
        if egg2[0]<1:
            continue
        egg1[0]-=egg2[1]
        egg2[0]-=egg1[1]
        f(x+1)
        egg1[0]+=egg2[1]
        egg2[0]+=egg1[1]

n=int(input())
egg=[]
answer=0
for _ in range(n):
    egg.append(list(map(int, input().split())))
f(0)
print(answer)