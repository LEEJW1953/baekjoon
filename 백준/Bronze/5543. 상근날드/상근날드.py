arr=[]
for i in range(5):
    arr.append(int(input()))
print(min(arr[0:3])+min(arr[3:5])-50)