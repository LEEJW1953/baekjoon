import sys
input=sys.stdin.readline

count1=1
count2=0

def fib(n):
    global count1
    if n==1 or n==2:
        return 1
    else:
        count1+=1
        return fib(n-1)+fib(n-2)

def fibo(n):
    global count2
    f=[1, 1]
    for i in range(2, n):
        f.append(f[i-1]+f[i-2])
        count2+=1
    return f[n-1]

n=int(input())
fib(n)
fibo(n)
print(count1, count2)