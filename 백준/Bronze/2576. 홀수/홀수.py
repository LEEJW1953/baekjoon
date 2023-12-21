arr=[]
for i in range(7):
    n=int(input())
    if n%2:
        arr.append(n)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)