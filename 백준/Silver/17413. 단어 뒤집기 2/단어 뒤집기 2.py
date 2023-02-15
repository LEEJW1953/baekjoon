import sys
input=sys.stdin.readline
from collections import deque

s=input().strip()
tmp=""
arr=[]
arr1=[]
for i in range(len(s)):
    if s[i]=="<":
        if arr1:
            arr1.reverse()
            arr.append(''.join(arr1))
            arr1=[]
        tmp+=s[i]
    elif s[i]==">":
        tmp+=s[i]
        arr.append(tmp)
        tmp=""
    else:
        if tmp!="":
            tmp+=s[i]
        elif s[i]==" ":
            arr1.reverse()
            arr.append(''.join(arr1))
            arr.append(" ")
            arr1=[]
        elif i==(len(s)-1):
            arr1.append(s[i])
            arr1.reverse()
            arr.append(''.join(arr1))
        else:
            arr1.append(s[i])
print(''.join(arr))