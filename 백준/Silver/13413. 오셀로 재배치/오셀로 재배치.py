import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    s1=input().strip()
    s2=input().strip()
    c1, c2 = 0, 0
    for i in range(n):
        if s1[i]!=s2[i]:
            if s1[i]=='W':
                c1+=1
            else:
                c2+=1
    print(max(c1, c2))