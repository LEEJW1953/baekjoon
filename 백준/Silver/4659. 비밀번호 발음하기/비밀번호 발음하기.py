import sys
input=sys.stdin.readline

def valid(s):
    vowel=False
    for i in range(len(s)):
        if s[i] in arr:
            vowel=True
        if 1<i:
            if s[i-2] not in arr and s[i-1] not in arr and s[i] not in arr:
                return False
            if s[i-2] in arr and s[i-1] in arr and s[i] in arr:
                return False
        if 0<i:
            if s[i-1]==s[i]:
                if s[i-1]=='e' and s[i]=='e':
                    pass
                elif s[i-1]=='o' and s[i]=='o':
                    pass
                else:
                    return False
    return vowel

arr=['a', 'e', 'i', 'o', 'u']
while True:
    s=input().strip()
    if s=='end':
        break
    if valid(s):
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')