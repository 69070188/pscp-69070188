"""vote"""
def main():
    """vote"""
    All = float(input())
    mx = float(input())
    mn = max(0,(All-mx)-mx)
    n = mx - mn
    if n > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
