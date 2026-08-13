"""ink"""
import math
def main():
    """ink"""
    PI = 3.1416
    S, N = map(int, input().split())
    results = []
    for _ in range(N):
        x, y = map(int, input().split())
        time = (PI * (x**2 + y**2)) / S
        results.append(math.ceil(time))
    for res in results:
        print(res)
main()

