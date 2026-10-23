"""b-fullypair"""
def main():
    """b-fullypair"""
    text = input()
    count = {}

    for char in text:
        count[char] = count.get(char, 0) + 1

    result = []
    for char in text:
        if count[char] % 2 == 1 and char not in result:
            result.append(char)

    if result:
        print("".join(result))
    else:
        print("fully paired")

main()
