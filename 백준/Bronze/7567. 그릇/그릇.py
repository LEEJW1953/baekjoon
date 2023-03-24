import sys
input=sys.stdin.readline

s=input().strip()
answer = 10
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        answer+=5
    else:
        answer+=10
print(answer)