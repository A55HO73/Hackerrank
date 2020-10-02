"""problem link https://www.hackerrank.com/challenges/sherlock-and-permutations/problem"""

"Fix 1 @ index 0 then calculate the possible ways of putting (M-1)s 1 and Ns 0 all at a time"






from math import factorial


def C(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def solve(m0, m1):
    m1 -= 1

    if m0 == 0 or m1 == 0:
        print(1)
    else:
        print(C(m0 + m1, m0) % 1000000007)


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    solve(m, n)
