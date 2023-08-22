t=int(input())
for i in range(t):
    n=int(input())
    arr1=input().split()
    arr2=input().split()
    password=input().split()
    loc=[]
    ans=[]
    for j in range(n):
        for k in range(n):
            if arr2[k]==arr1[j]:
                loc.append(k)
                break
    for j in range(n):
        ans.append(password[loc[j]])
    print(*ans)