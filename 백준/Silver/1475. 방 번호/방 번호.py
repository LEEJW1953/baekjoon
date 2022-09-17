n=input()
arr=[0]*10
for i in n:
    arr[int(i)]+=1
arr[6]=(arr[6]+arr[9]+1)//2
arr[9]=0
print(max(arr))