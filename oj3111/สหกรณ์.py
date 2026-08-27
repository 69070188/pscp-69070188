"""สหการณ์"""
def main():
    """สหการณ์"""
    a = input()
    b = int(input())
    total = 0
    for _ in range(b):
        c = float(input())
        total = total + c
    if a == "Y":
        yes = total - (total * 0.05) + 0.001
        print(f"{yes:.2f}")
    elif a == "N" and total >= 500:
        no = total - (total * 0.03) +0.001
        print(f"{no:.2f}")
    else:
        total = total + 0.001
        print(f"{total:.2f}")
main()
