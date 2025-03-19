import sys
def atm_time(n):
    numbers = list(map(int, input().split()))
    numbers.sort()

    total=0
    current=0
    for i in numbers:
        current+=i
        total+=current
    return total
n=int(sys.stdin.readline())
print(atm_time(n))