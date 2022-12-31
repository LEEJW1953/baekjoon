a, b=map(int, input().split())
n=a-a*(b/100)
if n<100:
    print(1)
else:
    print(0)