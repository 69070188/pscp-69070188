"""blackbrige"""
def main():
    """blackbrige"""
    a = int(input())
    b = int(input())
    goal = int(input())

    use_big = min(b, goal // 5)
    remaining_length = goal - (use_big * 5)

    if a >= remaining_length:
        print(remaining_length)
    else:
        print(-1)
main()
