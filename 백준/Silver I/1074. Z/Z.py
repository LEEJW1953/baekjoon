import sys
input=sys.stdin.readline

def z(x, i, j, ans):
    if x==1:
        if i-2==r and j-2==c:
            print(ans-3)
        elif i-2==r and j-1==c:
            print(ans-2)
        elif i-1==r and j-2==c:
            print(ans-1)
        elif i-1==r and j-1==c:
            print(ans)
    else:
        nx=2**(x-1)
        nnx=2**(2*(x-1))
        if r<i-nx and c<j-nx:
            z(x-1, i-nx, j-nx, ans-3*nnx)
        elif r<i-nx and j-nx<=c:
            z(x-1, i-nx, j, ans-2*nnx)
        elif i-nx<=r and c<j-nx:
            z(x-1, i, j-nx, ans-nnx)
        else:
            z(x-1, i, j, ans)

n, r, c = map(int, input().split())
z(n, 2**n, 2**n, 2**(2*n)-1)