import string

x = int(input())
l =[]
for _ in range(x) :
    l.append(input())
d= {}
for words in l :
    if words not in d :
        d[words] = 1
    else :
        d[words] += 1 
print(len(d.keys()))
print(*d.values(), sep =" ")
    
