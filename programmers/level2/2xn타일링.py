def solution(n):
    init = [0 for _ in range(n + 1)]
    init[0] = 0
    init[1] = 1
    init[2] = 2

    if n <= 2:
        return n
    else:
        for i in range(3, n + 1):
            init[i] = (init[i - 1] + init[i - 2]) % 1000000007
    return init[n] % 1000000007

# def solution(n):
#     a, b = 1, 1
#     for i in range(1, n):
#         a, b = b, (a + b) % 1000000007
#     return b