import sys
input=sys.stdin.readline
from itertools import combinations

def team(arr1, arr2):
    global answer
    team1=0
    team2=0
    for i in range(n//2):
        for j in range(n//2):
            team1+=g[arr1[i]][arr1[j]]
    for i in range(n//2):
        for j in range(n//2):
            team2+=g[arr2[i]][arr2[j]]
    answer=min(abs(team1-team2), answer)
    return

answer=int(1e9)
n=int(input())
g=[list(map(int, input().split())) for _ in range(n)]
com=list(combinations(range(n), n//2))
for i in range(len(com)//2):
    team(com[i], com[len(com)-1-i])
    if answer==0:
        break
print(answer)