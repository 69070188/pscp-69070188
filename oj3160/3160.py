"""jum"""
x,y = input().split()
x = int(x)
y = int(y)
total = []
for i in range(x,y+1):
    if i == 2:
        total.append(i)
    elif i == 1:
        pass
    elif i == 3:
        total.append(i)
    elif i == 5:
        total.append(i)
    elif i == 7:
        total.append(i)
    elif not i % 2: #ถ้าหารแล้วเศษเหลือ 0 จะไม่เป็นจำนวนเฉพาะ
        pass
    elif not i % 3: #ถ้าหารแล้วเศษเหลือ 0 จะไม่เป็นจำนวนเฉพาะ
        pass
    elif not i % 5: #ถ้าหารแล้วเศษเหลือ 0 จะไม่เป็นจำนวนเฉพาะ
        pass
    elif not i % 7: #ถ้าหารแล้วเศษเหลือ 0 จะไม่เป็นจำนวนเฉพาะ
        pass
    elif not i%i and not i%1: #จำนวนเฉพาะคือหารแค่ตัวมันเองและ 1 แล้วเหลือเศษ 0
        total.append(i)
if not total:
    print(f"Total primes: {len(total)}")
else:
    print(*total)# *total คือ ลบ [] ออก
    print(f"Total primes: {len(total)}")
