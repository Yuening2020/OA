def solve(line):
    stack = []
    result = [' '] * len(line)

    for i in range(len(line)):
        if line[i] == '(':
            stack.append(i)
        elif line[i] == ')':
            if stack:
                stack.pop()
            else:
                result[i] = '?'

    while stack:
        index = stack.pop()
        result[index] = 'x'
    
    print(line)
    print(''.join(result))      


# 在此改input数值
line = '))))UUUU((()'
solve(line)

