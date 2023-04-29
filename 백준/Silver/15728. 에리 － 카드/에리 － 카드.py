import sys
input=sys.stdin.readline

n, k = map(int, input().split())
share=list(map(int, input().split()))
team=list(map(int, input().split()))
share.sort()
team.sort()
for _ in range(k):
    maxx=max(share[0]*team[0],share[-1]*team[-1],share[-1]*team[0],share[0]*team[-1])
    if maxx==share[0]*team[0] or maxx==share[-1]*team[0]:
        team.pop(0)
    else:
        team.pop()
print(max(share[0]*team[0],share[-1]*team[-1],share[-1]*team[0],share[0]*team[-1]))