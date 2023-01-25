def star(m):
    if m == 1:
        return ['*']

    Stars = star(m//3) 
    arr = []  
    for i in Stars:
        arr.append(i*3)
    for i in Stars:
        arr.append(i+' '*(m//3)+i)
    for i in Stars:
        arr.append(i*3)
    return arr

n = int(input())
print('\n'.join(star(n)))