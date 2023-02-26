import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    arr=[list(map(int, input().split())) for _ in range(4)]
    arr.sort()
    m1=((arr[3][1]-arr[0][1])**2+(arr[3][0]-arr[0][0])**2)**0.5
    m2=((arr[2][1]-arr[1][1])**2+(arr[2][0]-arr[1][0])**2)**0.5
    s1=((arr[3][1]-arr[1][1])**2+(arr[3][0]-arr[1][0])**2)**0.5
    s2=((arr[3][1]-arr[2][1])**2+(arr[3][0]-arr[2][0])**2)**0.5
    s3=((arr[1][1]-arr[0][1])**2+(arr[1][0]-arr[0][0])**2)**0.5
    s4=((arr[2][1]-arr[0][1])**2+(arr[2][0]-arr[0][0])**2)**0.5
    if m1==m2 and (s1==s2==s3==s4):
        print(1)
    else:
        print(0)