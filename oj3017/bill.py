"""bill"""
def main():
    """bill"""
    a = int(input())
    b = a*0.1
    if b <= 50:
        b = 50
    elif b >= 1000:
        b = 1000
    c = a + b
    d = c + (c*0.07)
    print(f'{d:.2f}')
main()
