"""แปลงดอกไม้"""
import math as m
def main():
    """แปลงดอกไม้"""
    x, y = map(int, input().split())
    count = 1
    floor = 0
    multiplier = 1
    while count <= y:
        count += multiplier
        multiplier += 1
        floor += 1
    print(m.ceil(floor / x))

main()
