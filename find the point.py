"""problem link https://www.hackerrank.com/challenges/find-point/problem"""






t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    x=2*a[2]-a[0]
    y=2*a[3]-a[1]
    print(x ,y)
