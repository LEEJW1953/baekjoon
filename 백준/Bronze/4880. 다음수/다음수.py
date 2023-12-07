import sys
input=sys.stdin.readline

while True:
    a,b,c=map(int,input().split())
    if not a and not b and not c:
        break
    if c-b==b-a:
        print(f'AP {c+b-a}')
    else:
        print(f'GP {c*(c//b)}')