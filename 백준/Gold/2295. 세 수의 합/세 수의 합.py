import sys
input=sys.stdin.readline

n=int(input())
u=[]
answer={}
for i in range(n):
    u.append(int(input()))
u=list(set(u))
two=set()
for i in range(n):
    for j in range(n):
        two.add(u[i]+u[j])
for i in range(len(u)):
    for j in range(len(u)):
        if (u[i]-u[j]) in two:
            answer[u[i]]=(u[i], u[j], u[i]-u[j])
print(sorted(list(answer.keys()))[-1])