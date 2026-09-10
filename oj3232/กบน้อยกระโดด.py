"""กบน้อยกระโดด"""
def main():
    """กบน้อยกระโดด"""
    x , y = input().split()
    x = int(x)
    y = int(y)
    total = 0
    jump = 0
    while total < y:
        if x <= 0:
            jump = -1
            break
        total += x
        jump += 1
        x -= 2
    print(jump)
main()
