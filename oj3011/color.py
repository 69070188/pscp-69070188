"""color"""
def main():
    """color"""
    colors1 = input()
    colors2 = input()
    if colors1 == "Red" and  colors2 == "Yellow":
        print("Orange")
    elif colors1 == "Red" and  colors2 == "Blue":
        print("Violet")
    elif colors1 == "Red" and  colors2 == "Red":
        print("Red")
    elif colors1 == "Yellow" and  colors2 == "Red":
        print("Orange")
    elif colors1 == "Yellow" and  colors2 == "Blue":
        print("Green")
    elif colors1 == "Yellow" and  colors2 == "Yellow":
        print("Yellow")
    elif colors1 == "Blue" and  colors2 == "Red":
        print("Violet")
    elif colors1 == "Blue" and  colors2 == "Yellow":
        print("Green")
    elif colors1 == "Blue" and  colors2 == "Blue":
        print("Blue")
    else:
        print("Error")
main()
