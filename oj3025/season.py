"""winter"""
def main():
    """"winter"""
    month = int(input())
    day = int(input())
    season = ""
    z = month % 3
    if month in (1,2,3):
        season = "winter"
    elif month in (4,5,6) :
        season = "spring"
    elif month in (7,8,9) :
        season = "summer"
    elif month in (10,11,12) :
        season = "fall"
    if not z and day >= 21:
        if season == "winter":
            print("spring")
        elif season == "spring":
            print("summer")
        elif season == "summer":
            print("fall")
        elif season == "fall":
            print("winter")
    else:
        print(season)
main()
