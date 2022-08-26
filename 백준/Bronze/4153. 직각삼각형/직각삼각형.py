while True:
    x,y,z=map(int, input().split())
    if x==0:
        break
    a=max(x,y,z)
    arr=[x,y,z]
    arr.remove(a)
    if a**2==(arr[0]**2)+(arr[1]**2):
        print('right')
    else:
        print('wrong')