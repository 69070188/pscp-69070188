"""สงครามส่งด่วน"""
def main():
    """สงครามส่งด่วน"""
    a,b = input().split()
    c = float(input())
    if a == "BKK" and b == "CNX":
        bath1 = (c*30)+10
        print(f"{bath1:.2f}")
    elif a == "CNX" and b == "UBP":
        bath2 = (c*40)+15
        print(f"{bath2:.2f}")
    elif a == "UBP" and b == "BKK":
        bath3 = (c*40)+20
        print(f"{bath3:.2f}")
    elif a == "BKK" and b == "PKT":
        bath4 = (c*50)+25
        print(f"{bath4:.2f}")
    elif a == "PKT" and b == "CNX":
        bath5 = (c*60)+30
        print(f"{bath5:.2f}")
    elif a == "UBP" and b == "PKT":
        bath6 = (c*70)+40
        print(f"{bath6:.2f}")
    else:
        print("Error")
main()
