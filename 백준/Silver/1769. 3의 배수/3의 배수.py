import sys
input=sys.stdin.readline

n=input().strip()
count=0
while 10<=int(n):
    n=str(sum(list(map(int, n))))
    count+=1
print(count)
if int(n)%3:
    print('NO')
else:
    print('YES')