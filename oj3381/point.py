"""point"""
t = int(input())
ti = 0
while ti < t:
    n = int(input())
    pts = []
    i = 0
    while i < n:
        parts = input().split()
        x = int(parts[0])
        y = int(parts[1])
        pts.append((x, y))
        i += 1

    i = 0
    while i < len(pts) - 1:
        j = i + 1
        while j < len(pts):
            p1 = pts[i]
            p2 = pts[j]
            f1 = p1[0] + p1[1]
            f2 = p2[0] + p2[1]

            swap = False
            if f1 > f2:
                swap = True
            elif f1 == f2 and p1[1] < p2[1]:
                swap = True

            if swap:
                tmp = pts[i]
                pts[i] = pts[j]
                pts[j] = tmp
            j += 1
        i += 1

    for p in pts:
        print(str(p[0]) + " " + str(p[1]))
    ti += 1
