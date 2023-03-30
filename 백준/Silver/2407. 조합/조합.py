n, m =  map(int, input().split())
s=1
for i in range(n, n-m, -1):
    s*=i
for i in range(1, m+1):
    s//=i
print(s)