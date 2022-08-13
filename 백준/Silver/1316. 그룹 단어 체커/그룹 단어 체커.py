n=int(input())
count=0
for i in range(n):
    word=input()
    add=0
    for j in range(len(word)-1):
        if word[j+1]!=word[j]:
            word1=word[j+1:]
            if word1.count(word[j])>0:
                add+=1
    if add==0:
        count+=1
print(count)