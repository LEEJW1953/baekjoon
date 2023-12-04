a,b=map(int, input().split())
a,b=min(a,b),max(a,b)
print(b-a-1 if b!=a else 0)
for i in range(a+1, b):
    print(i, end=' ')