arr1=['a','i','y','e','o','u']
arr2=['b','k','x','z','n','h','d','c','w','g','p','v','j','q','t','s','r','l','m','f']
d={}
while True:
    try:
        s=input()
        ans=''
        for i in range(6):
            d[ord(arr1[i])]=ord(arr1[i-3])
            d[ord(arr1[i])-32]=ord(arr1[i-3])-32
        for i in range(len(arr2)):
            d[ord(arr2[i])]=ord(arr2[i-10])
            d[ord(arr2[i])-32]=ord(arr2[i-10])-32
        for i in s:
            if ord(i) in d:
                ans+=chr(d[ord(i)])
            else:
                ans+=i
        print(ans)
    except:
        break