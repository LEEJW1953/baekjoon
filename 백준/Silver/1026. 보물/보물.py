import sys
input=sys.stdin.readline

n=int(input())
aa=list(map(int, input().split()))
bb=list(map(int, input().split()))
aa.sort()
bb.sort()
result=0
for i in range(n):
    result+=aa[i]*bb[n-1-i]
print(result)