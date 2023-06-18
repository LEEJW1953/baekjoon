import sys
input=sys.stdin.readline
from itertools import combinations

t=input().strip()
target=[0]*26
total=[0]*26
prices=[]
word=[]
ans=10**9
for i in t:
    target[ord(i)-65]+=1
n=int(input())
for i in range(n):
    price, book = input().split()
    prices.append(int(price))
    tmp=[0]*26
    for j in book:
        tmp[ord(j)-65]+=1
        total[ord(j)-65]+=1
    word.append(tmp)
for i in range(26):
    if total[i]<target[i]:
        print(-1)
        exit(0)
for i in range(n):
    for j in combinations(range(n), i+1):
        tmp=[0]*26
        canMake=True
        totalPrice=0
        for k in range(i+1):
            totalPrice+=prices[j[k]]
        if ans<totalPrice:
            continue
        for k in range(i+1):
            for l in range(26):
                tmp[l]+=word[j[k]][l]
        for k in range(26):
            if tmp[k]<target[k]:
                canMake=False
                break
        if canMake:
            ans=min(ans, totalPrice)
print(ans)