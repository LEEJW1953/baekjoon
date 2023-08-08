import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    s=input().split()
    sound=[]
    while True:
        cry=input().strip()
        if cry=='what does the fox say?':
            break
        sound.append(cry.split()[2])
    for j in s:
        if j not in sound:
            print(j, end=' ')
    print()