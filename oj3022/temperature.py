"""temp"""
def main():
    """temp"""
    n = float(input())
    x = input()
    y = input()
    C = 0
    kelvin = 0
    Celsius1 = n - 273.15
    Celsius2 = (n-32)/1.8
    Celsius3 = ((n*5)/9 )- 273.15
    Fahrenheit = 0
    Rankine = 0

    if x == "C":
        C = n
    elif x == "F":
        C = Celsius2
    elif x == "K":
        C = Celsius1
    elif x == "R":
        C = Celsius3

    if y == "C":
        print(f'{C:.2f}')
    elif y == "F":
        Fahrenheit = ((C*9)/5)+32
        print((f'{Fahrenheit:.2f}'))
    elif y == "K":
        kelvin = C + 273.15
        print((f'{kelvin:.2f}'))
    elif y == "R":
        Rankine = ((C+273.15)*9)/5
        print((f'{Rankine:.2f}'))

main()
