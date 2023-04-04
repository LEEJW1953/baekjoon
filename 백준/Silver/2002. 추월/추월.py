import sys
input=sys.stdin.readline

n=int(input())
car=dict()
answer=0
for i in range(n):
    car[input().strip()]=[i]
for i in range(n):
    car[input().strip()].append(i)
arr=list(car.values())
for i in range(n):
    for j in range(arr[i][0]):
        if arr[j][1]>arr[i][1]:
            answer+=1
            break
print(answer)