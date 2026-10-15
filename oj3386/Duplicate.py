"""Duplicate"""
def main():
    """Duplicate"""
    m = int(input())
    n = int(input())
    s1 = set()
    i = 0
    while i < m:
        s1.add(int(input()))
        i += 1
    s2 = set()
    i = 0
    while i < n:
        s2.add(int(input()))
        i += 1

    com = s1.intersection(s2)
    if not com:
        print("Nope")
    else:
        lst = list(com)
        lst.sort(reverse=True)
        for x in lst:
            print(x)
main()
