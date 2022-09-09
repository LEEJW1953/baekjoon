import sys
# input=sys.stdin.readline().strip

def recursion(s, l, r):
    global count
    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else:
        count+=1 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count+=1
    return recursion(s, 0, len(s)-1)

t=int(input())
for i in range(t):
    count=0
    ss=sys.stdin.readline().strip()
    print(isPalindrome(ss), count)