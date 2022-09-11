import sys
input=sys.stdin.readline

n=int(input())
dis=list(map(int, input().split()))
price=list(map(int, input().split()))
price.pop()
result=0
min=price[0]
for i in range(n-2):
    if min<=price[i+1]:
        result+=min*dis[i]
    else:
        result+=min*dis[i]
        min=price[i+1]
result+=min*dis[n-2]
print(result)