import itertools

k, m = map(int, input().split())
array = []
for _ in range(k):
    array.append(list(map(int, input().split()))[1:])
    
result = 0
for combination in itertools.product(*array):
    result = max(sum([x * x for x in combination]) % m, result)
print(result)
