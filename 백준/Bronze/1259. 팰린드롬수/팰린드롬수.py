import sys
input=sys.stdin.readline

while True:
    n=input().strip()
    result=True
    if n=='0':
        break
    else:
        if len(n)%2==0:
            for i in range(len(n)//2):
                if n[i]!=n[len(n)-1-i]:
                    result=False
                    break
        else:
            for i in range(len(n)//2):
                if n[i]!=n[len(n)-1-i]:
                    result=False
                    break
    if result:
        print('yes')
    else:
        print('no')