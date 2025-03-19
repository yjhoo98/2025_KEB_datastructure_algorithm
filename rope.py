import sys
def rope_sol(n):
    if n>=1 and n<=100000:
        rope_weight = [int(sys.stdin.readline()) for _ in range(n)]
        rope_weight.sort(reverse=True)
        return max(rope_weight[i] * (i + 1) for i in range(n))
    else:
        return None

n = int(sys.stdin.readline())

print(f'{rope_sol(n)}')