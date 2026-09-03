"""3135"""
def main():
    """3135"""
    n, k, t = input().split()
    n = int(n)
    k = int(k)
    t = int(t)
    if t == 1:
        print(1)
        return
    current = 1
    count = 1
    while True:
        next_per = (current - 1 + k) % n + 1
        if next_per == 1:
            break
        if next_per == t:
            count += 1
            break
        count += 1
        current = next_per
    print(count)
main()
