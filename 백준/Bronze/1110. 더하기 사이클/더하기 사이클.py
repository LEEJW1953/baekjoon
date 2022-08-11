n=int(input())
m=n
n=(n%10)*10+(((n//10)+(n%10))%10)
a=1
while n!=m:
    n=(n%10)*10+(((n//10)+(n%10))%10)
    a+=1
print(a)