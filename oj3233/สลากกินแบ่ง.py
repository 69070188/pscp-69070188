"""สลากกินแบ่ง"""
def main():
    """สลากกินแบ่ง"""
    x1,y1 = input().split()
    x2,y2 = input().split()

    youlast2y1_3 = y1[2]
    youlast2y2_4 = y2[3]
    youlast2y1_5 = y1[4]

    melast2y2_3 = y2[2]
    melast2y2_4 = y2[3]
    melast2y2_5 = y2[4]

    total = 0

    if x1 == x2 and y1 == y2:
        total += 1000000
    elif x1 != x2 and y1 == y2:
        total += 100000
    elif x1 == x2 and youlast2y1_3 == melast2y2_3 \
          and youlast2y2_4 == melast2y2_4 and youlast2y1_5 == melast2y2_5 :
        total += 2000
    elif x1 == x2 and youlast2y2_4 == melast2y2_4 and youlast2y1_5 == melast2y2_5:
        total += 1000
    elif x1 != x2 and youlast2y1_3 == melast2y2_3 \
        and youlast2y2_4 == melast2y2_4 and youlast2y1_5 == melast2y2_5:
        total += 200
    elif x1 != x2 and youlast2y2_4 == melast2y2_4 and youlast2y1_5 == melast2y2_5:
        total += 100
    elif x1 == x2 :
        total += 20
    else:
        total += 0

    print(total)
main()
