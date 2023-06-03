import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    s1, s2 = map(str, input().split())
    arr1=[0]*26
    arr2=[0]*26
    result=''
    for i in s1:
        arr1[ord(i)-97]+=1
    for i in s2:
        arr2[ord(i)-97]+=1
    for i in range(26):
        if arr1[i]!=arr2[i]:
            result='NOT '
            break
    print(f'{s1} & {s2} are {result}anagrams.')