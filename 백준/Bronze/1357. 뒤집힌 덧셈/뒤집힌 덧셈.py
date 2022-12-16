def rev(n):
    s=str(n)
    s1=s[::-1]
    return int(s1)

x, y = map(int, input().split())
print(rev(rev(x)+rev(y)))