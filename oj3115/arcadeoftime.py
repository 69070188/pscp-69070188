"""Arcade"""
def main():
    """Arcade"""
    amount, check = map(int, input().split())
    minutes = [0] * 1441

    for _ in range(amount):
        start, stop = map(int, input().split())
        for i in range(start, stop):
            minutes[i] += 1

    check_time = input().split()
    result = []

    for i in range(check):
        t = int(check_time[i])
        result.append(str(minutes[t]))
    print(" ".join(result))

main()
