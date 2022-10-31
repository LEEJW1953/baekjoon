import sys
input=sys.stdin.readline

l=int(input())
string=input().strip()
result=0
i=0
for s in string:
    result+=(ord(s)-96)*31**(i)
    i+=1
print(result%1234567891)