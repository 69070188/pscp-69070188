"""game"""
def main():
    """game"""
    x = int(input())
    total = 0
    for _ in range(x):
        y = input()
        if y == "+":
            total += 10
        elif y == "-":
            total -= 5
    print(total)
main()
