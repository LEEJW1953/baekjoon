t=int(input())
for i in range(t):
    a,b=map(str, input().split())
    a=int(a)
    for i in range(len(b)):
        if i!=(len(b)-1):
            print(a*b[i],end='')
        if i==(len(b)-1):
            print(a*b[i])