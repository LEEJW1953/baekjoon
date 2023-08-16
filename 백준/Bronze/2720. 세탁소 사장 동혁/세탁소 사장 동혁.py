t=int(input())
for i in range(t):
    n=int(input())
    q=n//25
    n-=q*25
    d=n//10
    n-=d*10
    ni=n//5
    n-=ni*5
    print(f'{q} {d} {ni} {n}')