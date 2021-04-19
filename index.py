from math import sqrt

try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    equation = ""
    if a != 0:
        equation += f'{a}X^2'

    if b != 0:
        if b > 0 and a != 0:
            equation += "+"
        equation += f'{b}X'

    if c != 0:
        if c > 0:
            equation += "+"
        equation += str(c)

    print(equation + '=0')
    delta = b*b-4*a*c
    if a == 0:
        print(f'The solution to this equation is x:{(c)/(b)}')
    else:
        if delta > 0:
            print(
                f'The solutions to this equation are x1: {((-b)+ sqrt(delta))/(2*a)}    |    x2: {((-b)- sqrt(delta))/(2*a)}')
        elif delta == 0:
            print(f'The solution to this equation is x:{(-b)/(2*a)}')
        elif delta < 0:
            print('no solutions for thie equation')
except:
    print("Invild input")
