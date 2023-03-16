import sys
input=sys.stdin.readline
from itertools import permutations

def inning(hit, num, k):
    out=0
    i=num
    scr=0
    b1, b2, b3 = 0, 0, 0
    while out<3:
        if arr[k][hit[i]]==0:
            out+=1
        elif arr[k][hit[i]]==4:
            scr+=b1+b2+b3+1
            b1, b2, b3 = 0, 0, 0
        elif arr[k][hit[i]]==1:
            if b3:
                scr+=1
            b1, b2, b3 = 1, b1, b2
        elif arr[k][hit[i]]==2:
            scr+=b2+b3
            b1, b2, b3 = 0, 1, b1
        elif arr[k][hit[i]]==3:
            scr+=b1+b2+b3
            b1, b2, b3 = 0, 0, 1
        i+=1
        if i==9:
            i=0
    return scr, i

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
answer=0
for hit in permutations(range(1, 9), 8):
    hit=list(hit)
    hit.insert(3, 0)
    score=0
    tmp=0
    for i in range(n):
        cur, hitter = inning(hit, tmp, i)
        tmp=hitter
        score+=cur
        if score+24*(n-i-1)<answer:
            break
    if score>answer:
        answer=score
print(answer)