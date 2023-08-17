import sys
input=sys.stdin.readline
from itertools import permutations

def check(arr):
    if arr[0]+arr[2]+arr[5]+arr[7]!=26:
        return False
    if arr[0]+arr[3]+arr[6]+arr[10]!=26:
        return False
    if arr[7]+arr[8]+arr[9]+arr[10]!=26:
        return False
    if arr[1]+arr[2]+arr[3]+arr[4]!=26:
        return False
    if arr[1]+arr[5]+arr[8]+arr[11]!=26:
        return False
    if arr[4]+arr[6]+arr[9]+arr[11]!=26:
        return False
    return True

def show(star1):
    star=[]
    for i in star1:
        star.append(chr(i+64))
    print(f'....{star[0]}....')
    print(f'.{star[1]}.{star[2]}.{star[3]}.{star[4]}.')
    print(f'..{star[5]}...{star[6]}..')
    print(f'.{star[7]}.{star[8]}.{star[9]}.{star[10]}.')
    print(f'....{star[11]}....')
    return

star=[]
blank=[1]*12
target=[]
for i in range(5):
    arr=list(input().strip())
    for j in arr:
        if j=='.':
            continue
        if j=='x':
            star.append(0)
        else:
            star.append(ord(j)-64)
for i in range(12):
    if star[i]:
        blank[star[i]-1]=0
for i in range(12):
    if blank[i]:
        target.append(i+1)
for i in permutations(target, len(target)):
    star1=star[:]
    j=0
    for k in range(12):
        if not star1[k]:
            star1[k]=i[j]
            j+=1
    if check(star1):
        show(star1)
        exit(0)