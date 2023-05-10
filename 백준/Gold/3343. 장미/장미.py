import sys
input=sys.stdin.readline
import math

n, a, b, c, d = map(int, input().split())
total=int(1e19)
ans=1e16
if b*c<a*d:
    a, b, c, d = c, d, a, b

for i in range(c):
    j=math.ceil((n-i*a)/c)
    isover=False
    if j<0:
        j=0
        isover=True
    ans=min(ans, i*b+j*d)
    if isover:
        break
print(ans)