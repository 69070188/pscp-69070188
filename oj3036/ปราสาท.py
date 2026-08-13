"""ปราสาท"""
import math
def main():
    """ปราสาท"""
    N = int(input())
    if N == 1:
        print(0)
    else:
        # หาชั้น R
        R = math.ceil(math.sqrt(N))
        # หาตำแหน่งคอลัมน์ C ในชั้นนั้น
        C = N - (R - 1) ** 2
        # ถ้า C เป็นเลขคี่ (ชี้ขึ้น) ตอบ 2*(R-1)
        # ถ้า C เป็นเลขคู่ (ชี้ลง) ตอบ 2*(R-1) - 1
        if C % 2 == 1:
            print(2 * (R - 1))
        else:
            print(2 * (R - 1) - 1)
main()
