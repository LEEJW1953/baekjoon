import sys
input=sys.stdin.readline

while True:
    try:
        s, t = map(str, input().split())
        n1 = len(s)
        j=0
        for i in t:
            if i==s[j]:
                j+=1
            if j==n1:
                break
        if j==n1:
            print('Yes')
        else:
            print('No')
    except:
        break