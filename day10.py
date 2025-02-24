import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    list1 = [i for i in range(1, n + 1)]

    result = []
    index = 0
    while list1:
        index = (index + k - 1) % len(list1)
        result.append(list1.pop(index))

    print(f"<{', '.join(map(str, result))}>")
