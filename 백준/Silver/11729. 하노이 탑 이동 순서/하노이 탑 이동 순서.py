n=int(input())
print(2**n-1)

def han(n, start, end):
    if n==1:
        return print(start, end)

    han(n-1, start, 6-start-end)
    print(start, end)
    han(n-1, 6-start-end, end)

han(n, 1, 3)