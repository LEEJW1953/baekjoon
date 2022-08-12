word=input().upper()
arr=[]
for i in list(set(word)):
    count=word.count(i)
    arr.append(count)
if arr.count(max(arr))>=2:
    print('?')
else:
    print(list(set(word))[arr.index(max(arr))])