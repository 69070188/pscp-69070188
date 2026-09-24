"""RGB Mixed"""
def main():
    """RGB Mixed"""
    x1,x2,x3 = input().split()
    y1,y2,y3 = input().split()

    r1 = (int(x1)+int(y1))//2
    r2 = (int(x2)+int(y2))//2
    r3 = (int(x3)+int(y3))//2

    print(f"{r1} {r2} {r3}")

main()
