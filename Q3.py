from itertools import combinations

def mean(a):
    return sum(a) / len(a)

def median(a):
    n = len(a)
    if n % 2 == 0:
        return (a[n // 2 - 1] + a[n // 2]) / 2
    else:
        return a[n // 2]

def max_weight_value(n, a):
    a.sort()
    max_val = float('-inf')
    
    for r in range(1, n+1):
        for combination in combinations(a, r):
            max_val = max(max_val, mean(combination) - median(list(combination)))
    
    return max_val


# 在此改input数值
n = 4
a = [1, 5, 3, 9]
print(max_weight_value(n, a))