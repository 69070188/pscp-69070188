"""giraffe"""
def main():
    """giraffe"""
    n = int(input())
    l = []
    i = 0
    while i < n:
        l.append(int(input()))
        i += 1

    c = 0
    i = 0
    while i < n:
        if not i:
            if n == 1 or l[0] > l[1]:
                c += 1
        elif i == n - 1:
            if l[n - 1] > l[n - 2]:
                c += 1
        else:
            if l[i] > l[i - 1] and l[i] > l[i + 1]:
                c += 1
        i += 1
    print(c)
main()
