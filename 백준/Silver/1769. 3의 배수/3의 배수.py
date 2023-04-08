import sys
input=sys.stdin.readline

n=list(map(int, input().strip()))
c=0
while len(n)>1:
    n=list(map(int, str(sum(n))))
    c+=1
print(c)
if sum(n)%3:
    print('NO')
else:
    print('YES')