import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n, m = map(int, input().split())
    count=0
    for j in range(n, m+1):
        for k in str(j):
            if k=='0':
                count+=1
    print(count)