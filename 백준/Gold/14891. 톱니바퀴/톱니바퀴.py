import sys
input=sys.stdin.readline

def f(gearnum, move):
    if gearnum==0:
        if g[0][2]!=g[1][6]:
            if g[1][2]!=g[2][6]:
                if g[2][2]!=g[3][6]:
                    g[3]=rotate(g[3], -move)
                g[2]=rotate(g[2], move)
            g[1]=rotate(g[1], -move)
        g[0]=rotate(g[0], move)
    elif gearnum==1:
        if g[1][6]!=g[0][2]:
            g[0]=rotate(g[0], -move)
        if g[1][2]!=g[2][6]:
            if g[2][2]!=g[3][6]:
                g[3]=rotate(g[3], move)
            g[2]=rotate(g[2], -move)
        g[1]=rotate(g[1], move)
    elif gearnum==2:
        if g[2][2]!=g[3][6]:
            g[3]=rotate(g[3], -move)
        if g[2][6]!=g[1][2]:
            if g[1][6]!=g[0][2]:
                g[0]=rotate(g[0], move)
            g[1]=rotate(g[1], -move)
        g[2]=rotate(g[2], move)
    elif gearnum==3:
        if g[3][6]!=g[2][2]:
            if g[2][6]!=g[1][2]:
                if g[1][6]!=g[0][2]:
                    g[0]=rotate(g[0], -move)
                g[1]=rotate(g[1], move)
            g[2]=rotate(g[2], -move)
        g[3]=rotate(g[3], move)
    return

def rotate(gear, dir):
    new_gear=''
    arr1=[7,0,1,2,3,4,5,6]
    arr2=[1,2,3,4,5,6,7,0]
    for i in range(8):
        if dir==1:
            new_gear+=gear[arr1[i]]
        elif dir==-1:
            new_gear+=gear[arr2[i]]
    return new_gear

g=[]
answer=0
for i in range(4):
    g.append(input().strip())
k=int(input())
for i in range(k):
    a, b = map(int, input().split())
    f(a-1, b)
for i in range(4):
    answer+=2**i*int(g[i][0])
print(answer)