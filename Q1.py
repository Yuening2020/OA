def solve(source, target):
    count = 0
    cur = 0
    while cur < len(target):
        prev = cur
        index = 0
        while index < len(source) and cur < len(target):
            if source[index] == target[cur]:
                cur += 1
            index += 1
        
        if prev == cur:
            return -1
        count += 1
    
    return count


# 在此改input数值
source = 'xyz'
target = 'xzyxz'
    
print(solve(source, target))