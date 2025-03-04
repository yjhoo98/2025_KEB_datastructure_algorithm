import sys
import math

def turret(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # 두 원의 중심 거리

    if x1 == x2 and y1 == y2 and r1 == r2:  # 두 원이 완전히 일치
        return -1
    elif d > r1 + r2 or d < abs(r1 - r2):  # 만나지 않음 (외부 또는 내부)
        return 0
    elif d == r1 + r2 or d == abs(r1 - r2):  # 한 점에서 만남 (외접, 내접)
        return 1
    else:  # 두 점에서 만남
        return 2

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

    result = []
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
        result.append(str(turret(x1, y1, r1, x2, y2, r2)))

    # 한 번에 출력 (출력 초과 방지)
    sys.stdout.write("\n".join(result) + "\n"