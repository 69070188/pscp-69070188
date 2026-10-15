"""padtai"""
ing = []
while True:
    try:
        s = input().strip()
    except EOFError:
        break
    if s == "Cook":
        break
    if s:
        ing.append(s)

flav = []
while True:
    try:
        s = input().strip()
    except EOFError:
        break
    if s == "End":
        break
    if s:
        flav.append(s)

allowed = [
    "Pad Thai Sauce",
    "Tofu",
    "Pickle Turnip",
    "Shrimp",
    "Bean Sprouts",
    "Noodle",
    "Chives",
    "Lime",
    "Egg",
    "Oil",
    "Peanuts"
]

has_invalid = False
for x in ing:
    if x not in allowed:
        has_invalid = True
        break

if has_invalid:
    print("This is not Pad Thai!!!")
else:
    all_present = True
    for a in allowed:
        found = False
        for x in ing:
            if x == a:
                found = True
                break
        if not found:
            all_present = False
            break

    if not all_present:
        print("This is bad!")
    else:
        sweet = False
        sour = False
        salty = False
        other = False

        for f in flav:
            if f == "Sweet":
                sweet = True
            elif f == "Sour":
                sour = True
            elif f == "Salty":
                salty = True
            else:
                other = True

        unique_flavs = set(flav)
        if sweet and sour and salty and not other and len(unique_flavs) == 3:
            print("Delicious!")
        else:
            print("Not Bad...")
