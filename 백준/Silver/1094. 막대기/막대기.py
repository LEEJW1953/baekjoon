import sys
input=sys.stdin.readline

x=int(input())
res=0
for i in str(bin(x)[2:]):
    res+=int(i)
print(res)