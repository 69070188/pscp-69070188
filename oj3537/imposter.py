"""Among Us"""
def main():
    """Among Us"""
    members = {}
    dead = {}

    while True:
        data = input()
        if data == "Start":
            break
        data = data.replace("{", "").replace("}", "")
        name, role = data.split(":")
        name = name.strip().strip('"').strip("'")
        role = role.strip().strip('"').strip("'")
        members[name] = role

    while True:
        name = input()
        if name == "End":
            break
        if name in members:
            dead[name] = members.pop(name)

    impostor = sum(1 for role in members.values()
                   if role == "Impostor")
    print(impostor, "Impostor Remains")

    print("***Alive***")
    for name, role in sorted(members.items()):
        print(f"{name} : {role}")

    print("***Dead***")
    for name, role in sorted(dead.items()):
        print(f"{name} : {role}")

main()
