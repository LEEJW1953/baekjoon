import sys
input=sys.stdin.readline

def binary(x, st, en):
    mid=(st+en)//2
    if en-st==1 or en==st:
        if x==two[mid]:
            return True
        else:
            return False
    elif x==two[mid]:
        return True
    elif x<two[mid]:
        return binary(x, st, mid)
    elif x>two[mid]:
        return binary(x, mid, en)
    return

n=int(input())
u=[]
answer=0
for i in range(n):
    u.append(int(input()))
u=list(set(u))
u.sort()
two=[]
for i in range(n):
    for j in range(n):
        two.append(u[i]+u[j])
two=list(set(two))
two.sort()
for i in range(len(u)):
    for j in range(i+1):
        if binary((u[i]-u[j]), 0, len(two)):
            answer=max(answer, u[i])
print(answer)