import sys
input=sys.stdin.readline

n, m = map(int, input().split())
one, six = 1e9, 1e9
line=[]
for _ in range(m):
    a, b = map(int, input().split())
    one=min(one, b)
    six=min(six, a)
    line.append([a, b])
if one<=(six/6):
    print(one*n)
    n=0
else:
    ans=six*(n//6)
    n%=6
    if one*n<six:
        ans+=one*n
    else:
        ans+=six
    print(ans)