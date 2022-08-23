n, m=map(int, input().split())
s=[]
s1=[]
for i in range(n):
    s.append(input())
for i in range(m):
    s1.append(input())
count=0
for i in range(len(s1)):
    if s1[i] in s:
        count+=1
print(count)