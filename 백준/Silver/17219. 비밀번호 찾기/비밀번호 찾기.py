import sys
input=sys.stdin.readline

n, m = map(int, input().split())
d={}
for i in range(n):
    site, password = map(str, input().split())
    d[site]=password
for i in range(m):
    print(d[input().strip()])