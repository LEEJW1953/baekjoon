import sys
input=sys.stdin.readline
from collections import defaultdict

while True:
    s=input().strip()
    if s=='*':
        break
    if len(s)==1:
        print(f'{s} is surprising.')
    else:
        n=len(s)
        isSurprising=True
        for i in range(1, n):
            d=defaultdict(int)
            for j in range(0, n-i):
                t=s[j:j+i+1]
                tmp=t[0]+t[-1]
                d[tmp]+=1
                if d[tmp]>1:
                    isSurprising=False
                    break
        if isSurprising:
            print(f'{s} is surprising.')
        else:
            print(f'{s} is NOT surprising.')