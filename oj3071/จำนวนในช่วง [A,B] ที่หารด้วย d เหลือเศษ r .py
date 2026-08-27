"""[LEARNING LOGS] Mod Range"""
def main():
    """[LEARNING LOGS] Mod Range"""
    a = int(input())
    b = int(input())
    d = int(input())
    r = int(input())
    result = 0
    for i in range(a, b + 1):
        if i % d == r:
            result = result + 1
    print(result)
main()
