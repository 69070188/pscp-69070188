"""ไพ่44"""
def main():
    """ไพ่44"""
    card = input()
    pointcard = card[:-1]#อันนี้คือเอาทุกตัวยกเว้นตัวสุดท้าย
    lastcard = card[-1]#อันนี้คือเอาตัวสุดท้าย
    pointcard = pointcard.upper()
    lastcard = lastcard.upper()

    if pointcard == "A":
        pointname = "ace"
    elif pointcard == "J":
        pointname = "jack"
    elif pointcard == "Q":
        pointname = "queen"
    elif pointcard == "K":
        pointname = "king"
    else:
        pointname = pointcard

    if lastcard == "D":
        lastname = "diamonds"
    elif lastcard == "H":
        lastname = "hearts"
    elif lastcard == "S":
        lastname = "spades"
    elif lastcard == "C":
        lastname = "clubs"
    else:
        lastname = lastcard
    print(f"{pointname} of {lastname}")
main()
