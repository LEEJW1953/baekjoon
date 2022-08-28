import sys
input=sys.stdin.readline

def GCD(a, b):
    while(b):
        a, b=b, a%b
    return a

def LCM(a, b):
    return (a*b)//GCD(a, b)

n=int(input())
arr=list(map(int, input().split()))
for i in range(1, n):
    print(arr[0]//GCD(arr[0], arr[i]), end='')
    print('/', end='')
    print(arr[i]//GCD(arr[0], arr[i]))