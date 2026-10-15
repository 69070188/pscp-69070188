"""shorten"""
res = ""
st = -1
ed = -1
has = False
while True:
    x = input()
    v = int(x)
    if v == -1:
        break
    if not has:
        st = v
        ed = v
        has = True
    else:
        if v == ed + 1:
            ed = v
        else:
            p = ""
            if st == ed:
                p = str(st)
            else:
                p = str(st) + "-" + str(ed)
            if not res:
                res = p
            else:
                res += ", " + p
            st = v
            ed = v
if has:
    p = ""
    if st == ed:
        p = str(st)
    else:
        p = str(st) + "-" + str(ed)
    if not res:
        res = p
    else:
        res += ", " + p
print(res)
