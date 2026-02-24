def climb_stairs(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(3, n + 1):
        temp = b
        b = a + b
        a = temp
    return b

n = 3
print(climb_stairs(n))