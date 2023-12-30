import sys
input=sys.stdin.readline

n=int(input())
vowel=['a','e','i','o','u']
s1=input().strip()
s2=input().strip()
if s1[0]!=s2[0] or s1[-1]!=s2[-1]:
    print('NO')
    exit(0)
t1, t2 = '', ''
d1, d2 = [0]*26, [0]*26
for i in s1:
    d1[ord(i)-97]+=1
    if i not in vowel:
        t1+=i
for i in s2:
    d2[ord(i)-97]+=1
    if i not in vowel:
        t2+=i
if sum(d1)==max(d1) or sum(d2)==max(d2):
    print('NO')
    exit(0)
for i in range(26):
    if d1[i]!=d2[i]:
        print('NO')
        exit(0)
if t1!=t2:
    print('NO')
else:
    print('YES')