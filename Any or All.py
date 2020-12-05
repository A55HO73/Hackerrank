n = int(input())
l = input().split()
print(any( i == i [::-1] for i in l)and all(int(i) >= 0 for i in l))
