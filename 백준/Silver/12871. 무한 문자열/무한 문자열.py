import math
import sys
input=sys.stdin.readline

s=input().strip()
t=input().strip()
a, b = len(s), len(t)
c=math.lcm(a, b)
a=c//a
b=c//b
if s*a==t*b:
    print(1)
else:
    print(0)