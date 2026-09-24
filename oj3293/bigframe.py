"""big frame"""
def main():
    """big frame"""
    x = input()
    most = len(x)
    n = []
    n.append(x)

    for _ in range(4):
        nn = input()
        if len(nn) > most:
            most = len(nn)
        n.append(nn)

    print("*"*(most+4))

    for i in range(5):
        print(f"* {n[i]} {" "*(most-len(n[i]))}*")
    print("*"* (most+4))


main()
